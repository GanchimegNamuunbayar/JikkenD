import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.cluster import hierarchy

def save_dendrogram(slope_matrices, species_names, output_dir):
    combined_df = pd.concat(slope_matrices, axis=1)
    # 生物間の距離行列を計算
    distance_matrix = hierarchy.distance.pdist(combined_df.T, metric='euclidean')
    # 階層的クラスタリングを実行
    linkage_matrix = hierarchy.linkage(distance_matrix, method='average')
    # Dendrogramをプロットして保存
    plt.figure(figsize=(12, 8))
    dendrogram = hierarchy.dendrogram(linkage_matrix, labels=species_names, orientation='top')
    plt.title("Dendrogram - Species Clustering")
    plt.xlabel("Species")
    plt.ylabel("Distance")
    dendrogram_path = os.path.join(output_dir, "dendrogram_across_speciess.png")
    plt.savefig(dendrogram_path)
    plt.close()

# CSVファイルが保存されているディレクトリ
csv_dir = "csv"
csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

slope_matrices = []
species_names = []

# 各CSVファイルを処理
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file, index_col=0)
    slopes = []
    for amino_acid in df.columns:
        slope, _, _, _, _ = linregress(df.index, df[amino_acid])
        slopes.append(slope)
    slope_matrices.append(pd.DataFrame(slopes, index=df.columns, columns=[species_name]))
    species_names.append(species_name)

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Dendrogramを保存
save_dendrogram(slope_matrices, species_names, output_dir)


import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering

def save_hierarchical_clustering(df, output_dir, species_name):
    # 階層的クラスタリング
    clustering = AgglomerativeClustering(n_clusters=5).fit(df)
    linkage_matrix = hierarchy.linkage(clustering.children_, method='average')
    
    # デンドログラムを作成して保存
    dendrogram_path = os.path.join(output_dir, f"dendrogram.png")
    plt.figure(figsize=(10, 8))
    hierarchy.dendrogram(linkage_matrix, labels=df.index.tolist(), leaf_rotation=90)
    plt.title(f"Hierarchical Clustering Dendrogram - {species_name}")
    plt.xlabel("Protein")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.savefig(dendrogram_path)
    plt.close()





# CSVファイルが保存されているディレクトリ
csv_dir = "csv"
csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

# 各CSVファイルを処理
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file)
    output_dir = os.path.join("plots", species_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # 階層的クラスタリングのデンドログラムを保存
    save_hierarchical_clustering(df, output_dir, species_name)

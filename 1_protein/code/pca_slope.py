import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.stats import linregress
from sklearn.preprocessing import StandardScaler

def save_pca_plot(slope_matrices, species_names, output_dir):
    combined_df = pd.concat(slope_matrices, axis=1)
    # データを標準化する
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(combined_df.T)
    # PCAを実行する
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)
    # 結果をDataFrameに格納
    pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'], index=species_names)
    # PCAの結果をプロットして保存
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue=pca_df.index, palette='Set1', s=100)
    plt.title("PCA Plot - Species Comparison")
    plt.xlabel("Principal Component 1 (PC1)")
    plt.ylabel("Principal Component 2 (PC2)")
    plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
    pca_plot_path = os.path.join(output_dir, "pca_plot_across.png")
    plt.savefig(pca_plot_path, bbox_inches='tight')
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

# PCAプロットを保存
save_pca_plot(slope_matrices, species_names, output_dir)

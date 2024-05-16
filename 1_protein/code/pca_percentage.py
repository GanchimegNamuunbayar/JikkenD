import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering

def save_pca_across_species(df_dict, output_dir):
    # 各生物のPCA結果をリストに格納
    pca_results = []
    for species_name, df in df_dict.items():
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(df)
        # インデックスを1次元に変換してDataFrameを作成
        pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'], index=[species_name] * len(df))
        pca_results.append(pca_df)

    # 全ての生物のPCA結果を結合
    combined_pca_df = pd.concat(pca_results)

    # PCAプロットを作成して保存
    pca_plot_path = os.path.join(output_dir, "pca_plot_across_species.png")
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=combined_pca_df, x='PC1', y='PC2', hue=combined_pca_df.index, palette='tab10', s=100)
    plt.title("PCA Plot Across Species")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.tight_layout()
    plt.savefig(pca_plot_path)
    plt.close()

# 以前のコードと同じ


# CSVファイルが保存されているディレクトリ
csv_dir = "csv"
csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

# 各生物のデータフレームを辞書に格納
df_dict = {}
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file, index_col=0)
    df_dict[species_name] = df

# PCAを生物間で実行してプロットを保存
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)
save_pca_across_species(df_dict, output_dir)

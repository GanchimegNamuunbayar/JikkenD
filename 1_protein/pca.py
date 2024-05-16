import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering

def save_pca_with_clustering(df, output_dir, species_name, sample_size=50):
    # ランダムにサンプリング
    sample_df = df.sample(n=min(sample_size, len(df)), random_state=42)
    
    # 主成分分析
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(sample_df)
    pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'], index=sample_df.index)
    
    # 階層的クラスタリング
    clustering = AgglomerativeClustering(n_clusters=3).fit(pca_df)
    sample_df['Cluster'] = clustering.labels_

    # PCAプロットを作成して保存
    pca_plot_path = os.path.join(output_dir, "pca_plot_with_clustering.png")
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue=sample_df['Cluster'], palette='tab10', s=100)
    plt.title(f"PCA Plot with Clustering - {species_name}")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.tight_layout()
    plt.savefig(pca_plot_path)
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
    
    # 保存
    save_pca_with_clustering(df, output_dir, species_name)

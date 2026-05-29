import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from paths import PROTEIN_CSV, PROTEIN_FIGURES, PROTEIN_PLOTS, RAW_PROTEIN

import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def save_pca(df, output_dir, species_name, sample_size=100):
    # ランダムにサンプリング
    sample_df = df.sample(n=min(sample_size, len(df)), random_state=42)
    
    # 主成分分析
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(sample_df)
    pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'], index=sample_df.index)
    
    # PCAプロットを作成して保存
    pca_plot_path = output_dir / "pca_plot.png"
    plt.figure(figsize=(10, 8))
    plt.scatter(pca_df['PC1'], pca_df['PC2'])
    plt.title(f"PCA Plot - {species_name}")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.savefig(pca_plot_path)
    plt.close()

# CSVファイルが保存されているディレクトリ
csv_dir = PROTEIN_CSV
csv_files = glob.glob(str(csv_dir / "*.csv"))

# 各CSVファイルを処理
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file, index_col=0)  # インデックスを設定
    output_dir = PROTEIN_PLOTS / species_name
    os.makedirs(output_dir, exist_ok=True)
    
    # 保存
    save_pca(df, output_dir, species_name)


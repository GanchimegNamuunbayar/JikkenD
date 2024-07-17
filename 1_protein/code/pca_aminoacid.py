import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def save_pca_plot(df, output_dir, species_name):
    print(f"Processing species: {species_name}")  # デバッグポイント
    print("Initial DataFrame:")
    print(df.head())  # デバッグポイント

    # 'Length'列を含めて標準化するためのデータ準備
    lengths = df['Length']
    df = df.drop(columns=['Length'])


    # データを標準化する
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.T)

    
    # 主成分分析
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)
    
    pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2'])
    pca_df['Amino Acid'] = df.columns

    # PCAプロットを作成して保存
    pca_plot_path = os.path.join(output_dir, "pca_amino_acid.png")
    plt.figure(figsize=(12, 10))
    sns.scatterplot(data=pca_df, x='PC1', y='PC2', s=100)
    for i, row in pca_df.iterrows():
        plt.text(row['PC1']+1, row['PC2']+1, row['Amino Acid'], fontsize=18, ha='right')
    plt.title(f"PCA Plot - {species_name}", fontsize=22)
    plt.xlabel("Principal Component 1 (Contribution: {:.2f}%)".format(pca.explained_variance_ratio_[0]*100), fontsize=20)
    plt.ylabel("Principal Component 2 (Contribution: {:.2f}%)".format(pca.explained_variance_ratio_[1]*100), fontsize=20)
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
    output_dir = os.path.join("output", species_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # 保存
    save_pca_plot(df, output_dir, species_name)

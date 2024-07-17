import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file_path = '../output/ro_2base.xlsx'
df = pd.read_excel(excel_file_path)

# Dinucleotide列をインデックスとして設定
df.set_index('Dinucleotide', inplace=True)

# 生物種の列を取得（最初の列はDinucleotideなのでそれ以降の列を取得）
species_columns = df.columns

scaler = StandardScaler()
standardized_data = scaler.fit_transform(df[species_columns].T)


# PCAの実行
pca = PCA(n_components=2)  # 2次元に次元削減
pca_result = pca.fit_transform(standardized_data)  # PCAを生物種方向に適用

explained_var_ratio = pca.explained_variance_ratio_

# 結果をDataFrameに変換して表示
pca_df = pd.DataFrame(pca_result, index=species_columns, columns=['PC1', 'PC2'])
print("PCA Results:")
print(pca_df)

# PCAの結果をプロット
plt.figure(figsize=(10, 8))
plt.scatter(pca_df['PC1'], pca_df['PC2'], s=100)

for species, (pc1, pc2) in pca_df.iterrows():
    plt.text(pc1 + 0.01, pc2 + 0.01, species, fontsize=12)

plt.title('PCA of Species Similarity by Dinucleotide')
plt.xlabel(f'Principal Component 1 ({explained_var_ratio[0]*100:.2f}%)')
plt.ylabel(f'Principal Component 2 ({explained_var_ratio[1]*100:.2f}%)')
plt.grid(True)
plt.show()
# 保存するファイルのパス
#output_file_path = '../output/Thaliana/comparison_3base.png'
# グラフをファイルとして保存
#plt.savefig(output_file_path)
# グラフを表示せずに終了
#plt.close()
#print(f"Plot saved to {output_file_path}")



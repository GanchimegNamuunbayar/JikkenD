import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file_path = '../output/ro_3base_filtered.xlsx'
df = pd.read_excel(excel_file_path)

# Dinucleotide列をインデックスとして設定
df.set_index('Trinucleotide', inplace=True)

# データを転置して標準化する
scaler = StandardScaler()
standardized_data = scaler.fit_transform(df)

# PCAの実行
pca = PCA(n_components=2)  # 2次元に次元削減
pca_result = pca.fit_transform(standardized_data)

explained_var_ratio = pca.explained_variance_ratio_

# 結果をDataFrameに変換して表示
pca_df = pd.DataFrame(pca_result, index=df.index, columns=['PC1', 'PC2'])
print("PCA Results:")
print(pca_df)

# PCAの結果をプロット
plt.figure(figsize=(10, 8))
plt.scatter(pca_df['PC1'], pca_df['PC2'], s=100)

for trinucleotide, (pc1, pc2) in pca_df.iterrows():
    plt.text(pc1 + 0.01, pc2 + 0.01, trinucleotide, fontsize=12)

plt.title('PCA of Species Similarity')
plt.xlabel(f'Principal Component 1 ({explained_var_ratio[0]*100:.2f}%)')
plt.ylabel(f'Principal Component 2 ({explained_var_ratio[1]*100:.2f}%)')
plt.grid(True)
plt.show()

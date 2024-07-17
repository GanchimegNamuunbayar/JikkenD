import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file_path = '../output/ro_3base_filtered.xlsx'
df = pd.read_excel(excel_file_path)

# Trinucleotide列をインデックスとして設定
df.set_index('Trinucleotide', inplace=True)

# 生物種の列を取得（最初の列はTrinucleotideなのでそれ以降の列を取得）
species_columns = df.columns

# 生物種間の類似性行列を作成
similarity_matrix = df[species_columns]-1

# デンドログラムの描画
plt.figure(figsize=(25, 25))
g = sns.clustermap(similarity_matrix, cmap='coolwarm', method='average', metric='euclidean', annot=False, fmt=".2f", dendrogram_ratio=(0.1, 0.2))
plt.setp(g.ax_heatmap.get_yticklabels(), rotation=0, fontsize=8)  # y軸ラベルのフォントサイズを調整
plt.show()

# 保存するファイルのパス
#output_file_path = '../output/Thaliana/heatmap_3base_gray.png'
# グラフをファイルとして保存
#plt.savefig(output_file_path)
# グラフを表示せずに終了
#plt.close()
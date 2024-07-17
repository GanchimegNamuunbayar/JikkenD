import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Excelファイルのパス
input_path = '../xlsx/repeated/all_species_ratios.xlsx'

# データを読み込む
data = pd.read_excel(input_path, index_col=0).T

# ヒートマップの作成
plt.figure(figsize=(12, 8))
sns.clustermap(data, cmap='coolwarm', annot=True, fmt='.3f', cbar_kws={'label': 'Ratio'})

# タイトルとラベルの設定
plt.title('Heatmap of Repeated Nucleotide Ratios in Genome')
plt.xlabel('Nucleotide')
plt.ylabel('Species')

# ヒートマップを表示
plt.tight_layout()
plt.show()
 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file_path = '../output/Average_ratio.xlsx'
# エクセルファイルを読み込む
df = pd.read_excel(excel_file_path, index_col=0)


# ヒートマップを描画する
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap='coolwarm', cbar=True, linewidths=.5)
plt.title('Average Nucleotide Ratios excluding Y chromosome')
plt.xlabel('Nucleotide')

plt.show()
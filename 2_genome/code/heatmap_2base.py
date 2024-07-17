import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Excelファイルからデータを読み込む
excel_file_path = '../output/ro_2base.xlsx'
df = pd.read_excel(excel_file_path)


# Dinucleotide列をインデックスとして設定
df.set_index('Dinucleotide', inplace=True)

# clustermapの描画
plt.figure(figsize=(12, 10))
sns.clustermap(df, cmap='coolwarm', annot=True, fmt=".2f", figsize=(12, 10))

plt.show()

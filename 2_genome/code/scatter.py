import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file_path = '../output/ro_3base.xlsx'
df = pd.read_excel(excel_file_path)

# Dinucleotide列をインデックスとして設定
df.set_index('Dinucleotide', inplace=True)

# 生物種の列を取得（最初の列はDinucleotideなのでそれ以降の列を取得）
species_columns = df.columns

# ダイヌクレオチドのリストを取得
dinucleotides = df.index

# プロットの設定
plt.figure(figsize=(15, 10))

# 各ダイヌクレオチドごとにプロット
for i, dinucleotide in enumerate(dinucleotides):
    plt.subplot(4, 4, i + 1)  # プロットを4x4のサブプロットに配置
    plt.scatter(range(len(species_columns)), df.loc[dinucleotide], s=50)
    plt.title(dinucleotide)
    plt.xlabel('Species')
    plt.ylabel('Frequency')
    plt.xlim(0, 1.3)
    plt.xticks(range(len(species_columns)), species_columns, rotation=90)
    plt.tight_layout()

plt.suptitle('Distribution of Dinucleotide Frequencies Across Species', y=1.05, fontsize=16)
plt.show()



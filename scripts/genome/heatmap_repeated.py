import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from paths import (
    GENOME_CSV,
    GENOME_FIGURES,
    GENOME_SPECIES,
    GENOME_TABLES,
    GENOME_TABLES_CHR_LEN,
    GENOME_TABLES_CHR_RATIO,
    GENOME_TABLES_DI,
    GENOME_TABLES_MONO,
    GENOME_TABLES_REPEATED,
    GENOME_TABLES_TRI,
    RAW_GENOME,
)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Excelファイルのパス
input_path = GENOME_TABLES_REPEATED / "ll_species_ratios.xlsx"

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
 
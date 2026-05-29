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
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Excelファイルからデータを読み込む
excel_file_path = GENOME_TABLES / "Average_ratio.xlsx"
# エクセルファイルを読み込む
df = pd.read_excel(excel_file_path, index_col=0)


# ヒートマップを描画する
plt.figure(figsize=(10, 8))
sns.heatmap(df, annot=True, cmap='coolwarm', cbar=True, linewidths=.5)
plt.title('Average Nucleotide Ratios excluding Y chromosome')
plt.xlabel('Nucleotide')

plt.show()
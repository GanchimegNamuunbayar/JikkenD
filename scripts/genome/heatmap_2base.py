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
from sklearn.preprocessing import StandardScaler

# Excelファイルからデータを読み込む
excel_file_path = GENOME_TABLES / "ro_2base.xlsx"
df = pd.read_excel(excel_file_path)


# Dinucleotide列をインデックスとして設定
df.set_index('Dinucleotide', inplace=True)

# clustermapの描画
plt.figure(figsize=(12, 10))
sns.clustermap(df, cmap='coolwarm', annot=True, fmt=".2f", figsize=(12, 10))

plt.show()

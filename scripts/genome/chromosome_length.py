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
import matplotlib.pyplot as plt

df = pd.read_csv(GENOME_CSV / "Thaliana.csv")

# 染色体ごとの配列の長さを計算
df['Sequence Length'] = df['Sequence'].apply(len)

# 染色体の順序を設定
#chromosome_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y']

# 染色体の順序に従ってデータを並び替え
#df_sorted = df.set_index('Chromosome').loc[chromosome_order]

# プロット
plt.figure(figsize=(10, 6))
#df_sorted['Sequence Length'].plot(kind='bar', color='blue', alpha=0.7)
df['Sequence Length'].plot(kind='bar', color='blue', alpha=0.7)

plt.xlabel('Chromosome')
plt.ylabel('Sequence Length')
plt.title('Sequence Length per Chromosome (Homo sapiens)')
plt.xticks(rotation=90)  # X軸のラベルを回転させて読みやすくする
plt.show()

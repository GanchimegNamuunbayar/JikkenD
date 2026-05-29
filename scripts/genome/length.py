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
import os

# CSVファイルのパス
csv_file_path = GENOME_CSV / "Saccharomyces.csv"

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# 染色体ごとにゲノムの長さを計算
chromosome_lengths = df.groupby('Chromosome')['Sequence'].apply(lambda x: sum(len(seq) for seq in x))

# DataFrameとして整理
chromosome_lengths_df = pd.DataFrame(chromosome_lengths).reset_index()
chromosome_lengths_df.columns = ['Chromosome', 'GenomeLength']

# Excelファイルに出力
excel_output_path = GENOME_SPECIES / "Saccharomyces/chromosome_lengths.xlsx"
chromosome_lengths_df.to_excel(excel_output_path, index=False)

print(f"Chromosome genome lengths saved to {excel_output_path}")

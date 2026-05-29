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
from collections import Counter

def count_chr1_trinucleotides(df):
    trinucleotide_counts = Counter()
    chr1_df = df[pd.to_numeric(df['Chromosome'], errors='coerce') == 1]
    for seq in chr1_df['Sequence']:
        for i in range(len(seq) - 2):
            trinucleotide = seq[i:i+3]
            if 'N' not in trinucleotide:
                trinucleotide_counts[trinucleotide] += 1
    return trinucleotide_counts

csv_file_path = GENOME_CSV / "Musculus.csv"
df = pd.read_csv(csv_file_path)
trinucleotide_counts = count_chr1_trinucleotides(df)

total_bases = sum(trinucleotide_counts.values())

if total_bases == 0:
    print("No bases found for Chromosome 1.")
else:
    base_ratios = {base: trinucleotide_counts[base] / total_bases for base in trinucleotide_counts}

    # 結果をデータフレームに変換
    results_df = pd.DataFrame(base_ratios.items(), columns=['Trinucleotide', 'Observed Ratio'])
    excel_output_path = GENOME_SPECIES / "Musculus/3base_ratio.xlsx"  # 出力先のエクセルファイルのパス
    results_df.to_excel(excel_output_path, index=False)
    print(f"Results have been saved to {excel_output_path}")


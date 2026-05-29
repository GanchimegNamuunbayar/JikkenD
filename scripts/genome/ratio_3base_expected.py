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
import os

# Specify the engine for reading Excel files
df_2base = pd.read_excel(GENOME_SPECIES / "Thaliana/2base_ratio.xlsx", engine='openpyxl')
dinucleotide_ratios = {row['Dinucleotide']: row['Observed Ratio'] for _, row in df_2base.iterrows()}

df_1base = pd.read_excel(GENOME_SPECIES / "Thaliana/1base_ratio.xlsx", engine='openpyxl')
base_ratios = {row['Base']: row['Ratio'] for _, row in df_1base.iterrows()}

def calculate_trinucleotide_ratios(dinucleotide_ratios, base_ratios):
    trinucleotide_ratios = {}
    for b1 in 'ATGC':
        for b2 in 'ATGC':
            for b3 in 'ATGC':
                dinucleotide = f"{b1}{b2}"
                if dinucleotide in dinucleotide_ratios:
                    trinucleotide = f"{b1}{b2}{b3}"
                    trinucleotide_ratios[trinucleotide] = (dinucleotide_ratios[dinucleotide] * base_ratios[b3])
    return trinucleotide_ratios

# 3塩基頻度を計算
trinucleotide_ratios = calculate_trinucleotide_ratios(dinucleotide_ratios, base_ratios)

# 結果をデータフレームに変換
results_df = pd.DataFrame(list(trinucleotide_ratios.items()), columns=['Trinucleotide', 'Expected Ratio'])

# 新しいエクセルファイルとして保存
results_df.to_excel(GENOME_SPECIES / "Thaliana/expected_3base_ratio_2x1.xlsx", index=False)


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

csv_file_path = '../csv/Musculus.csv'
df = pd.read_csv(csv_file_path)
trinucleotide_counts = count_chr1_trinucleotides(df)

total_bases = sum(trinucleotide_counts.values())

if total_bases == 0:
    print("No bases found for Chromosome 1.")
else:
    base_ratios = {base: trinucleotide_counts[base] / total_bases for base in trinucleotide_counts}

    # 結果をデータフレームに変換
    results_df = pd.DataFrame(base_ratios.items(), columns=['Trinucleotide', 'Observed Ratio'])
    excel_output_path = '../output/Musculus/3base_ratio.xlsx'  # 出力先のエクセルファイルのパス
    results_df.to_excel(excel_output_path, index=False)
    print(f"Results have been saved to {excel_output_path}")


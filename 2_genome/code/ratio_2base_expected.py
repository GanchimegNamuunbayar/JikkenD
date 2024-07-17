import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

def count_chr1_nucleotides(df):
    chr1_frequency = Counter()
    # 1番目の染色体の配列を取得
    df['Chromosome'] = pd.to_numeric(df['Chromosome'], errors='coerce')
    chr1_df = df[df['Chromosome'] == 1]

    print(f"Number of rows with Chromosome 1: {len(chr1_df)}")  # デバッグ用の出力

    for _, row in chr1_df.iterrows():
        # 1塩基
        for base in row['Sequence']:
            if base != 'N':
                chr1_frequency[base] += 1
    
    return chr1_frequency

# CSVファイルのパス
csv_file_path = '../csv/Saccharomyces.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# 最初の数行を表示してデータの確認
print(df.head())

# 染色体ごとに1塩基の頻度を集計
chr1_frequency = count_chr1_nucleotides(df)

total_bases = sum(chr1_frequency.values())

# total_basesがゼロの場合のチェック
if total_bases == 0:
    print("No bases found for Chromosome 1.")
else:
    base_ratios = {base: chr1_frequency[base] / total_bases for base in 'ATGC'}
    dinucleotide_ratios = {f"{b1}{b2}": base_ratios[b1] * base_ratios[b2] for b1 in 'ATGC' for b2 in 'ATGC'}
    # 結果をデータフレームに変換
    results_df = pd.DataFrame(list(dinucleotide_ratios.items()), columns=['Dinucleotide', 'Expected Ratio'])

    excel_output_path = '../output/Saccharomyces/expected_2base_ratio.xlsx'
    results_df.to_excel(excel_output_path, index=False)

    print(f"Results have been saved to {excel_output_path}")

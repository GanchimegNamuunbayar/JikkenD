import pandas as pd
import re
import os
from glob import glob
from collections import Counter

# 繰り返しパターンをカウントする関数
def count_repeated_nucleotides(sequence):
    single_nucleotide_pattern = re.compile(r'([ATGC])\1{3}')  # ちょうど4つの同じ塩基
    dinucleotide_pattern = re.compile(r'(([ATGC]{2})\2{1})')  # ちょうど2つの塩基の繰り返し

    repeated_counts = Counter()
    
    # 単一ヌクレオチドのカウント
    single_matches = single_nucleotide_pattern.findall(sequence)
    repeated_counts.update(single_matches)
    
    # 2ヌクレオチドのカウント
    dinucleotide_matches = dinucleotide_pattern.findall(sequence)
    repeated_counts.update([match[0] for match in dinucleotide_matches])
    
    return repeated_counts

def count_chr1_repeated_nucleotides(df):
    repeated_counts = Counter()
    chr1_df = df[pd.to_numeric(df['Chromosome'], errors='coerce') == 1]
    genome_length = chr1_df['Sequence'].str.len().sum()  # ゲノムの長さを計算
    for seq in chr1_df['Sequence']:
        repeated_counts.update(count_repeated_nucleotides(seq))
    
    return repeated_counts, genome_length

# CSVファイルのパス
csv_files = glob('../csv/*.csv')

# 結果を格納する辞書
final_results = {}

for csv_file_path in csv_files:
    df = pd.read_csv(csv_file_path)
    
    # 生物種名をファイル名から取得
    species_name = os.path.splitext(os.path.basename(csv_file_path))[0]

    # 初期化
    if species_name not in final_results:
        final_results[species_name] = {}

    # 繰り返しヌクレオチドのカウント
    repeated_counts, genome_length = count_chr1_repeated_nucleotides(df)

    # 割合を計算し、結果を辞書に格納
    for nucleotide, count in repeated_counts.items():
        if len(nucleotide) > 1:  # 1塩基の繰り返しを除外
            ratio = count / genome_length
            final_results[species_name][nucleotide] = ratio

# 結果をデータフレームに変換
results_df = pd.DataFrame(final_results).T.fillna(0)

# Excelファイルとして保存
output_path = '../xlsx/repeated/all_species_ratios.xlsx'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
results_df.to_excel(output_path)

print(f"Results have been saved to {output_path}")
print("Processing completed.")


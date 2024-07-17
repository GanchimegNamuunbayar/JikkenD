import pandas as pd
import os

# CSVファイルのパス
csv_file_path = '../csv/Saccharomyces.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# 染色体ごとにゲノムの長さを計算
chromosome_lengths = df.groupby('Chromosome')['Sequence'].apply(lambda x: sum(len(seq) for seq in x))

# DataFrameとして整理
chromosome_lengths_df = pd.DataFrame(chromosome_lengths).reset_index()
chromosome_lengths_df.columns = ['Chromosome', 'GenomeLength']

# Excelファイルに出力
excel_output_path = '../output/Saccharomyces/chromosome_lengths.xlsx'
chromosome_lengths_df.to_excel(excel_output_path, index=False)

print(f"Chromosome genome lengths saved to {excel_output_path}")

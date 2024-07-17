import os
import glob
import pandas as pd
from collections import Counter

def count_nucleotides_by_chromosome(df):
    # 染色体ごとに1塩基の頻度を集計するための辞書
    frequencies_by_chromosome = {}

    # データフレームを染色体ごとに処理
    for _, row in df.iterrows():
        chromosome = row['Chromosome']
        sequence = row['Sequence'].upper()  # DNA配列を大文字に変換

        # 染色体ごとの頻度をカウントするための Counter オブジェクトを作成
        if chromosome not in frequencies_by_chromosome:
            frequencies_by_chromosome[chromosome] = Counter()
        
        # 1塩基ごとにカウントを更新
        for base in sequence:
            if base != 'N':
                frequencies_by_chromosome[chromosome][base] += 1
    
    return frequencies_by_chromosome

def calculate_cg_content(frequencies_by_chromosome):
    cg_contents = {}
    
    # 各染色体ごとにC+G含量の割合を計算
    for chromosome, counter in frequencies_by_chromosome.items():
        total_c = counter['C']
        total_g = counter['G']
        total_bases = sum(counter.values())
        
        # C+Gの割合を計算
        cg_content = (total_c + total_g) / total_bases if total_bases > 0 else 0
        cg_contents[chromosome] = cg_content
    
    return cg_contents

# CSVファイルのディレクトリ
csv_directory = '../csv'

# CSVファイルのリストを取得
csv_files = glob.glob(os.path.join(csv_directory, '*.csv'))

# 結果を保存するためのリスト
results = []

# 各CSVファイルを処理
for csv_file in csv_files:
    try:
        species_name = os.path.basename(csv_file).split(".")[0]
        print(f"Processing file: {csv_file}")  # デバッグ

        df = pd.read_csv(csv_file)
        df['Chromosome'] = pd.to_numeric(df['Chromosome'], errors='coerce')

        # 列名の確認
        if 'Chromosome' not in df.columns or 'Sequence' not in df.columns:
            print(f"Error: {csv_file} does not contain required columns 'Chromosome' and 'Sequence'")
            print(f"Columns found: {df.columns}")  # デバッグ
            continue

        frequencies_by_chromosome = count_nucleotides_by_chromosome(df)
        cg_contents = calculate_cg_content(frequencies_by_chromosome)
        
        for chromosome, cg_content in cg_contents.items():
            results.append([species_name, chromosome, cg_content])
    
    except Exception as e:
        print(f"An error occurred while processing {csv_file}: {e}")

# 結果をデータフレームに変換
results_df = pd.DataFrame(results, columns=['Species', 'Chromosome', 'CG_Content'])

# 結果をエクセルファイルに保存
output_excel_path = '../output/cg_content_by_chromosome.xlsx'
results_df.to_excel(output_excel_path, index=False)

print(f"Results saved to {output_excel_path}")

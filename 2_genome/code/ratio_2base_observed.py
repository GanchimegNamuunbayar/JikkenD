import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def count_chr1_dinucleotides(df):
    # ダイヌクレオチドの頻度をカウントするための Counter オブジェクト
    dinucleotide_counts = Counter()
    # 1番目の染色体の配列を取得
    df['Chromosome'] = pd.to_numeric(df['Chromosome'], errors='coerce')
    chr1_df = df[df['Chromosome'] == 1]

    for _, row in chr1_df.iterrows():
        sequence = row['Sequence']
        # 2塩基
        for i in range(len(sequence) - 1):
            dinucleotide = sequence[i:i+2]
            if 'N' not in dinucleotide:
                dinucleotide_counts[dinucleotide] += 1
    
    return dinucleotide_counts

# CSVファイルのパス
csv_file_path = '../csv/Saccharomyces.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# 1番目の染色体におけるダイヌクレオチドの頻度を集計
dinucleotide_counts = count_chr1_dinucleotides(df)

# 最初の数行を表示してデータの確認
print(df.head())

total_bases = sum(dinucleotide_counts.values())

# total_basesがゼロの場合のチェック
if total_bases == 0:
    print("No bases found for Chromosome 1.")
else:
    base_ratios = {base: dinucleotide_counts[base] / total_bases for base in ['AA', 'AT', 'AG', 'AC', 
                                                                              'TA', 'TT', 'TG', 'TC', 
                                                                              'GA', 'GT', 'GG', 'GC', 
                                                                              'CA', 'CT', 'CG', 'CC']}

    # 結果をデータフレームに変換
    results_df = pd.DataFrame(list(base_ratios.items()), columns=['Dinucleotide', 'Ratio'])

    excel_output_path = '../output/Saccharomyces/2base_ratio.xlsx'  # 出力先のエクセルファイルのパス
    results_df.to_excel(excel_output_path, index=False)

    print(f"Results have been saved to {excel_output_path}")




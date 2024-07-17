import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

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
        
        # 1塩基c
        for base in sequence:
            if base != 'N':
                frequencies_by_chromosome[chromosome][base] += 1
    
    return frequencies_by_chromosome

def calculate_nucleotide_ratios(frequencies_by_chromosome):
    # 塩基の割合を計算するための辞書
    ratios_by_chromosome = {}

    for chromosome, counter in frequencies_by_chromosome.items():
        total_bases = sum(counter.values())
        ratios_by_chromosome[chromosome] = {base: count / total_bases for base, count in counter.items()}
    
    return ratios_by_chromosome

# CSVファイルのパス
csv_file_path = '../csv/Chlamydomonas.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# 染色体ごとに1塩基の頻度を集計
frequencies_by_chromosome = count_nucleotides_by_chromosome(df)

# 塩基の割合を計算
ratios_by_chromosome = calculate_nucleotide_ratios(frequencies_by_chromosome)

# エクセルファイルに格納
excel_file_path = '../output/Chlamydomonas/Chromosome_Ratio.xlsx'
ratios_df = pd.DataFrame(ratios_by_chromosome).T
ratios_df.to_excel(excel_file_path)

# グラフを描画する
chromosomes = sorted(frequencies_by_chromosome.keys())
#chromosomes = ['1', '5', '10', '15', '19', 'X', 'Y']
bases = ['A', 'T', 'G', 'C']
x = range(len(chromosomes))

# 各染色体に対する塩基ごとの数を計算
ratios = {base: [ratios_by_chromosome[chromosome].get(base, 0) for chromosome in chromosomes] for base in bases}

# 棒グラフを描画
fig, ax = plt.subplots(figsize=(14, 7))
bar_width = 0.2
offsets = [-1.5, -0.5, 0.5, 1.5]  # 棒グラフのオフセット

for i, base in enumerate(bases):
    ax.bar([pos + offsets[i] * bar_width for pos in x], ratios[base], bar_width, label=base)

ax.set_xlabel('Chromosome')
ax.set_xticks(x)
ax.set_xticklabels(chromosomes)
ax.set_ylabel('Ratio')
ax.set_title('Nucleotide Ratios of Chlamydomonas')
ax.legend()
# x軸にグリッド線を追加
#plt.show()
# 保存するファイルのパス
output_file_path = '../output/Chlamydomonas/Chromosome_Ratio.png'

# グラフをファイルとして保存
plt.savefig(output_file_path)

# グラフを表示せずに終了
plt.close()

print(f"Plot saved to {output_file_path}")
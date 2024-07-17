import matplotlib.pyplot as plt
import pandas as pd
from adjustText import adjust_text
import numpy as np

# エクセルファイルのパス
excel_file_path = '../output/Chlamydomonas/3base_ratio.xlsx'


# エクセルファイルからデータを読み込む
df = pd.read_excel(excel_file_path)

complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# 逆相補鎖を作成する関数
def get_complement(trinucleotide):
    return ''.join(complement[base] for base in reversed(trinucleotide))

# トリヌクレオチドとその逆相補鎖のペアをセットに追加する
seen = set()
filtered_rows = []

for _, row in df.iterrows():
    trinucleotide = row['Trinucleotide']
    complement_seq = get_complement(trinucleotide)
    
    # トリヌクレオチドがセットにない場合のみ追加する
    if trinucleotide not in seen and complement_seq not in seen:
        filtered_rows.append(row)
        seen.add(trinucleotide)
        seen.add(complement_seq)

# フィルタリングされたデータフレームを作成する
filtered_df = pd.DataFrame(filtered_rows)
# Expected Ratio と Observed Ratio のデータを取得
expected_ratios = df['Expected Ratio']
observed_ratios = df['Observed Ratio']

trinucleotides = df['Trinucleotide']  # 三ヌクレオチドのラベル

plt.figure(figsize=(8, 6))
plt.scatter(expected_ratios, observed_ratios, marker='o', color='b')

#texts = []
#for i, tri in enumerate(trinucleotides):
    #texts.append(plt.text(expected_ratios[i], observed_ratios[i], tri, ha='center', va='center'))

#adjust_text(texts, arrowprops=dict(arrowstyle='-', color='black'), force_text=(0.1, False))  # force_textをタプルで指定する

plt.plot([0, max(expected_ratios)], [0, max(expected_ratios)], color='r', linestyle='--', label='Ideal line (y=x)')

plt.title('Observed Ratio vs Expected Ratio of Trinucleotide (Chlamydomonas)')
plt.xlabel('Expected Ratio')
plt.ylabel('Observed Ratio')
plt.legend()
plt.grid(True)
plt.tight_layout()
#plt.show()

# 保存するファイルのパス
output_file_path = '../output/Chlamydomonas/comparison_3base.png'
# グラフをファイルとして保存
plt.savefig(output_file_path)
# グラフを表示せずに終了
plt.close()

print(f"Plot saved to {output_file_path}")




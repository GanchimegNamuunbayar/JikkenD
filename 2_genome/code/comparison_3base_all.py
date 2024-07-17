import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from glob import glob

# エクセルファイルのパス
excel_file_paths = glob('../graph/3base ratio/*.xlsx')

complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
# 逆相補鎖を作成する関数
def get_complement(trinucleotide):
    return ''.join(complement[base] for base in reversed(trinucleotide))

fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(20, 15))  # 最大8つのサブプロット
axes = axes.flatten()

for i, excel_file in enumerate(excel_file_paths):
    if i >= 8:  # 最大8つのプロットを表示する
        break
    
    df = pd.read_excel(excel_file)
    
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
    expected_ratios = filtered_df['Expected Ratio']
    observed_ratios = filtered_df['Observed Ratio']
    trinucleotides = filtered_df['Trinucleotide']  # 三ヌクレオチドのラベル

    ax = axes[i]
    ax.scatter(expected_ratios, observed_ratios, marker='o', color='b')

    ax.plot([0, max(expected_ratios)], [0, max(expected_ratios)], color='r', linestyle='--', label='Ideal line (y=x)')

    ax.set_title(f'Observed vs Expected Ratios\n{os.path.basename(excel_file)}')
    ax.set_xlabel('Expected Ratio')
    ax.set_ylabel('Observed Ratio')
    ax.legend()
    ax.grid(True)

# 調整と保存
plt.tight_layout()
output_file_path = '../graph/comparison_3base_subplot.png'
plt.savefig(output_file_path)
plt.close()

print(f"Plot saved to {output_file_path}")

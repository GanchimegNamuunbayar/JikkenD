import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob
from adjustText import adjust_text

# エクセルファイルのパス
excel_file_paths = glob('../xlsx/3base ratio/*.xlsx')

complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# 逆相補鎖を作成する関数
def get_complement(trinucleotide):
    return ''.join(complement[base] for base in reversed(trinucleotide))

# フィギュアの設定
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

    max_ratio = max(max(expected_ratios), max(observed_ratios))
    ax.plot([0, max_ratio], [0, max_ratio], color='r', linestyle='--')
    file_basename = os.path.splitext(os.path.basename(excel_file))[0]
    ax.set_title(f'{file_basename}')
    #ax.set_xlabel('Expected Ratio')
    #ax.set_ylabel('Observed Ratio')
    ax.legend()
    ax.grid(True)

    # 確認のため注釈を追加
    for j, tri in enumerate(trinucleotides):
        ax.annotate(tri, (expected_ratios.iloc[j], observed_ratios.iloc[j]), fontsize=8, alpha=0.75)

# 調整と保存
plt.tight_layout()
output_file_path = '../graph/comparison_3base_subplot.png'
plt.savefig(output_file_path)
plt.show()  # 保存後にプロットを表示

print(f"Plot saved to {output_file_path}")

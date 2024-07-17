import pandas as pd

# エクセルファイルのパス
excel_file = '../output/Thaliana/3base_ratio.xlsx'

# エクセルファイルを読み込む
df = pd.read_excel(excel_file)

# 逆相補鎖の対応関係を定義する辞書
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

# 新しいエクセルファイルとして保存
filtered_df.to_excel('../output/Thaliana/3base_ratio_filtered.xlsx', index=False)

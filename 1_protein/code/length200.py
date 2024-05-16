import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルが保存されているディレクトリ
csv_dir = "csv"
csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

# 生物ごとにアミノ酸組成を格納するディクショナリを作成
amino_acid_composition_dict = {}

# 各CSVファイルを処理
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file)
    
    # タンパク質の長さが200の行をフィルタリング
    df_200 = df[df['Length'] == 200]
    
    # アミノ酸の組成を計算し、ディクショナリに追加
    amino_acid_composition = df_200.mean().drop(['Length'])
    amino_acid_composition_dict[species_name] = amino_acid_composition

# 結果をDataFrameに変換
amino_acid_composition_df = pd.DataFrame(amino_acid_composition_dict)

# 横棒グラフのプロット
plt.figure(figsize=(12, 8))
amino_acid_composition_df.T.plot(kind='barh', stacked=True)
plt.title('Amino Acid Composition (Protein Length = 200)')
plt.xlabel('Percentage')
plt.ylabel('Species')
plt.legend(title='Amino Acid', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
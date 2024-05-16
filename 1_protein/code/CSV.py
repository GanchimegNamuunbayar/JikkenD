import os
import glob
import pandas as pd
import numpy as np
from scipy.stats import linregress
from Bio import SeqIO

def process_fasta_file(fasta_file):
    # タンパク質の長さとアミノ酸組成のデータを準備
    protein_lengths = []
    amino_acid_counts = {aa: [] for aa in "ACDEFGHIKLMNPQRSTVWY"}
    
    # fastaファイルをパースしてデータを取得
    for record in SeqIO.parse(fasta_file, "fasta"):
        protein_lengths.append(len(record.seq))
        for aa in amino_acid_counts:
            count = record.seq.count(aa)
            amino_acid_counts[aa].append(count)
    
    # DataFrameに変換
    protein_lengths = np.array(protein_lengths)
    amino_acid_composition = pd.DataFrame(amino_acid_counts)
    
    # 各アミノ酸の割合を計算
    amino_acid_composition_percentage = amino_acid_composition.div(protein_lengths, axis=0) * 100
    
    # タンパク質の長さの範囲を制限
    mask = (protein_lengths >= 50) & (protein_lengths <= 200)
    filtered_lengths = protein_lengths[mask]
    filtered_composition_percentage = amino_acid_composition_percentage[mask]
    
    # 傾きを計算
    slopes = []
    for amino_acid in filtered_composition_percentage.columns:
        slope, _, _, _, _ = linregress(filtered_lengths, filtered_composition_percentage[amino_acid])
        slopes.append(slope)
    
    # 傾きに基づいてアミノ酸を並べ替える
    sorted_amino_acids = [x for _, x in sorted(zip(slopes, filtered_composition_percentage.columns), reverse=True)]
    
    # ソートされたアミノ酸に基づいてデータフレームを再構成
    sorted_composition_percentage = filtered_composition_percentage[sorted_amino_acids]
    
    # データフレームを作成
    filtered_data = pd.DataFrame(filtered_lengths, columns=['Length'])
    sorted_composition_percentage = sorted_composition_percentage.reset_index(drop=True)
    final_df = pd.concat([filtered_data, sorted_composition_percentage], axis=1)
    return final_df

# CSVファイルを保存するディレクトリを作成
csv_dir = "csv"
os.makedirs(csv_dir, exist_ok=True)

# faaディレクトリ内のすべての.faaファイルを処理
pathes = glob.glob("faa/*.faa")

for path in pathes:
    species = os.path.basename(path).split(".")[0]
    # 各faaファイルを処理
    final_df = process_fasta_file(path)
    # CSVファイルとして保存
    csv_path = os.path.join(csv_dir, f"{species}.csv")
    final_df.to_csv(csv_path, index=False)
    print(f"Saved {csv_path}")
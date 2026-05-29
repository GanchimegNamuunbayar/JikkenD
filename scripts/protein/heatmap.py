import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from paths import PROTEIN_CSV, PROTEIN_FIGURES, PROTEIN_PLOTS, RAW_PROTEIN

import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def save_heatmap(df, output_dir, species_name):
    # タンパク質の長さごとにアミノ酸の割合の平均を計算
    mean_df = df.groupby('Length').mean()
    # Heatmapを作成して保存
    heatmap_path = output_dir / f"heatmap.png"
    plt.figure(figsize=(10, 8))
    sns.heatmap(mean_df, cmap='coolwarm')
    plt.title(f"Heatmap - {species_name}")
    plt.xlabel("Amino Acid")
    plt.ylabel("Protein Length")
    plt.savefig(heatmap_path)
    plt.close()

# CSVファイルが保存されているディレクトリ
csv_dir = PROTEIN_CSV
csv_files = glob.glob(str(csv_dir / "*.csv"))

# 各CSVファイルを処理
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file)
    output_dir = PROTEIN_PLOTS / species_name
    os.makedirs(output_dir, exist_ok=True)
    
    # Heatmapを保存
    save_heatmap(df, output_dir, species_name)


import os
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import linregress

def save_combined_slope_heatmap(slope_matrices, species_names, output_dir):
    combined_df = pd.concat(slope_matrices, axis=1)
    plt.figure(figsize=(10, 8))
    sns.heatmap(combined_df, cmap='coolwarm', annot=True, fmt=".3f", cbar_kws={'label': 'Slope'})
    plt.title("Combined Slope Heatmap")
    plt.xlabel("Species")
    plt.ylabel("Amino Acid")
    heatmap_path = os.path.join(output_dir, "combined_slope_heatmap.png")
    plt.savefig(heatmap_path)
    plt.close()

# CSVファイルが保存されているディレクトリ
csv_dir = "csv"
csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

slope_matrices = []
species_names = []

# 各CSVファイルを処理
for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file, index_col=0)
    slopes = []
    for amino_acid in df.columns:
        slope, _, _, _, _ = linregress(df.index, df[amino_acid])
        slopes.append(slope)
    slope_matrices.append(pd.DataFrame(slopes, index=df.columns, columns=[species_name]))
    species_names.append(species_name)

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# Combined Slope Heatmapを保存
save_combined_slope_heatmap(slope_matrices, species_names, output_dir)

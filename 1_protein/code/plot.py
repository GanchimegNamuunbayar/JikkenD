import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from statsmodels.nonparametric.smoothers_lowess import lowess

def plot_and_save_graphs(df, species_name):
    # タンパク質の長さとアミノ酸の割合を取得
    filtered_lengths = df['Length']
    filtered_composition_percentage = df.drop(columns=['Length'])

    # 出力ディレクトリを作成
    output_dir = os.path.join("plots", species_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # 散布図のプロット
    fig, axes = plt.subplots(4, 5, figsize=(20, 16))
    axes = axes.flatten()
    for i, amino_acid in enumerate(filtered_composition_percentage.columns):
        ax = axes[i]
        ax.scatter(filtered_lengths, filtered_composition_percentage[amino_acid], label=amino_acid, alpha=0.5)
        ax.set_title(f'{amino_acid}')
        ax.set_xlim(50, 200)
        ax.set_xticks(range(50, 201, 50))
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Protein Length", labelpad=20, fontsize=14)
    plt.ylabel("Amino Acid(%)", labelpad=20, fontsize=14)
    plt.suptitle(f"{species_name}", fontsize=16)
    plt.tight_layout()
    scatter_plot_path = os.path.join(output_dir, "scatter_plot.png")
    plt.savefig(scatter_plot_path)
    plt.show()
    
    # 線形回帰のプロット
    fig, axes = plt.subplots(4, 5, figsize=(20, 16))
    axes = axes.flatten()
    for i, amino_acid in enumerate(filtered_composition_percentage.columns):
        ax = axes[i]
        slope, intercept, _, _, _ = linregress(filtered_lengths, filtered_composition_percentage[amino_acid])
        ax.plot(filtered_lengths, slope * filtered_lengths + intercept, label=amino_acid, alpha=0.5, color='r')
        ax.set_title(f'{amino_acid}')
        ax.set_xlim(50, 200)
        ax.set_xticks(range(50, 201, 50))
        ax.set_yticks(range(0, 11, 2))
        ax.set_ylim(0, 10)
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Protein Length", labelpad=20, fontsize=14)
    plt.ylabel("Amino Acid(%)", labelpad=20, fontsize=14)
    plt.suptitle(f"{species_name}", fontsize=16)
    plt.tight_layout()
    linear_regression_plot_path = os.path.join(output_dir, "linear_regression_plot.png")
    plt.savefig(linear_regression_plot_path)
    plt.show()

    # LOWESSのプロット
    fig, axes = plt.subplots(4, 5, figsize=(20, 16))
    axes = axes.flatten()
    for i, amino_acid in enumerate(filtered_composition_percentage.columns):
        ax = axes[i]
        smoothed = lowess(filtered_composition_percentage[amino_acid], filtered_lengths, frac=0.2)
        ax.plot(smoothed[:, 0], smoothed[:, 1], label=amino_acid, alpha=0.5, color='g')
        ax.set_title(f'{amino_acid}')
        ax.set_xlim(50, 200)
        ax.set_xticks(range(50, 201, 50))
        ax.set_yticks(range(0, 11, 2))
        ax.set_ylim(0, 10)
    fig.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Protein Length", labelpad=20, fontsize=14)
    plt.ylabel("Amino Acid(%)", labelpad=20, fontsize=14)
    plt.suptitle(f"{species_name}", fontsize=16)
    plt.tight_layout()
    lowess_plot_path = os.path.join(output_dir, "lowess_plot.png")
    plt.savefig(lowess_plot_path)
    plt.show()


current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# faaディレクトリの絶対パスを確認
csv_dir = os.path.abspath("csv")  # 現在のディレクトリの中にある 'faa' ディレクトリを指定
print(f"Expected FASTA directory: {csv_dir}")

# 実際のディレクトリの存在を確認
if not os.path.exists(csv_dir):
    print(f"Directory does not exist: {csv_dir}")
else:
    print(f"Directory exists: {csv_dir}")

# faaディレクトリ内のすべての.faaファイルを処理
pathes = glob.glob(os.path.join(csv_dir, "*.csv"))
print(f"Found files: {pathes}")

if not pathes:
    print("No .faa files found in the specified directory.")

# 各CSVファイルを処理
for csv_file in pathes:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file)
    plot_and_save_graphs(df, species_name)

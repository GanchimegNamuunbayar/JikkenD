import sys
from pathlib import Path as _Path

sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from paths import PROTEIN_CSV, PROTEIN_FIGURES, PROTEIN_PLOTS

import glob
import os

import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster import hierarchy
from sklearn.cluster import AgglomerativeClustering


def save_hierarchical_clustering(df, output_dir, species_name):
    clustering = AgglomerativeClustering(n_clusters=5).fit(df)
    linkage_matrix = hierarchy.linkage(clustering.children_, method="average")

    dendrogram_path = output_dir / "dendrogram.png"
    plt.figure(figsize=(10, 8))
    hierarchy.dendrogram(linkage_matrix, labels=df.index.tolist(), leaf_rotation=90)
    plt.title(f"Hierarchical Clustering Dendrogram - {species_name}")
    plt.xlabel("Protein")
    plt.ylabel("Distance")
    plt.tight_layout()
    plt.savefig(dendrogram_path)
    plt.close()


csv_files = glob.glob(str(PROTEIN_CSV / "*.csv"))

for csv_file in csv_files:
    species_name = os.path.basename(csv_file).split(".")[0]
    df = pd.read_csv(csv_file)

    for output_dir in (PROTEIN_PLOTS / species_name, PROTEIN_FIGURES / species_name):
        output_dir.mkdir(parents=True, exist_ok=True)
        save_hierarchical_clustering(df, output_dir, species_name)

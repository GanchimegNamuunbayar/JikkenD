# Comparative Genome Sequence Analysis

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

Portfolio repository for a university bioinformatics lab course: comparative analysis of **seven model organisms** using Python, public NCBI data, and standard omics workflows (statistics, visualization, clustering, PCA).

**Repository:** [comparative-genome-sequence-analysis](https://github.com/GanchimegNamuunbayar/comparative-genome-sequence-analysis)

## Overview

| Module | Focus |
|--------|--------|
| **Protein** | Proteome FASTA → amino-acid composition vs. length; length distributions; heatmaps; hierarchical clustering; PCA; cross-species comparison |
| **Genome** | Genomic DNA → mono-/di-/trinucleotide frequencies; observed vs. expected ratios; chromosome-level summaries; inter-species comparison |

Seven species: *Arabidopsis thaliana*, human, mouse, zebrafish, *Chlamydomonas*, *Cyanidioschyzon*, budding yeast.

## Project structure

```
comparative-genome-sequence-analysis/
├── data/
│   ├── raw/                    # FASTA downloads (gitignored extensions)
│   │   ├── protein/
│   │   └── genome/
│   └── processed/
│       ├── protein/            # Per-species amino-acid CSV tables
│       └── genome/             # Per-chromosome sequence CSV (generated)
├── scripts/
│   ├── paths.py                # Shared path constants
│   ├── protein/                # Protein analysis scripts
│   └── genome/                 # Genome analysis scripts
├── results/
│   ├── protein/
│   │   ├── figures/            # Main plots (density, PCA, dendrograms, …)
│   │   └── plots/              # Scatter / regression / LOWESS panels
│   └── genome/
│       ├── figures/            # Heatmaps, PCA, species comparison plots
│       ├── tables/             # Excel summaries (1/2/3-base, chromosome stats)
│       └── species/            # Per-species intermediate outputs (generated)
├── requirements.txt
└── README.md
```

## Species

| # | Organism | CSV / folder name |
|---|----------|-------------------|
| 1 | *Arabidopsis thaliana* | `thaliana` |
| 2 | Human | `homosapiens` |
| 3 | Mouse | `musculus` |
| 4 | Zebrafish | `zebrafish` |
| 5 | *Chlamydomonas* | `chlamydomonas` |
| 6 | *Cyanidioschyzon* | `cyanidioschyzon` |
| 7 | Budding yeast | `saccharomyces` |

## Setup

```bash
git clone https://github.com/GanchimegNamuunbayar/comparative-genome-sequence-analysis.git
cd comparative-genome-sequence-analysis

python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Data

1. Download proteome and genome FASTA from [NCBI Genome](https://www.ncbi.nlm.nih.gov/genome/).
2. Place files under `data/raw/protein/` and `data/raw/genome/` (see [data/raw/README.md](data/raw/README.md)).
3. Precomputed protein tables are included under `data/processed/protein/`.
4. Genome CSVs are produced locally with `scripts/genome/dna_csv.py` (edit input paths in the script).

Raw sequence files are excluded from git (size and NCBI terms).

## Running analyses

Scripts resolve paths via `scripts/paths.py` and can be run from the repository root or from each script folder.

### Protein workflow

```bash
# FASTA → CSV (place *.faa in data/raw/protein/)
python scripts/protein/CSV.py

# Length distribution (edit fasta path in script)
python scripts/protein/distribution.py

# Scatter, linear regression, LOWESS
python scripts/protein/plot.py

# Heatmaps, dendrograms, PCA
python scripts/protein/heatmap.py
python scripts/protein/dendrogram.py
python scripts/protein/pca.py

# Cross-species comparison
python scripts/protein/heatmap_comparison.py
python scripts/protein/dendrogram_comparison.py
```

Example outputs: `results/protein/figures/`, `results/protein/plots/`.

### Genome workflow

```bash
# FASTA → chromosome CSV
python scripts/genome/dna_csv.py

# Nucleotide frequencies
python scripts/genome/ratio_1base.py
python scripts/genome/ratio_2base_observed.py
python scripts/genome/ratio_2base_expected.py
python scripts/genome/ratio_3base_observed.py
python scripts/genome/ratio_3base_expected.py

# Visualization and comparison
python scripts/genome/heatmap_1base.py
python scripts/genome/comparison_all.py
python scripts/genome/pca_2base.py
```

Tables: `results/genome/tables/` (subfolders `mono_nucleotide`, `dinucleotide`, `trinucleotide`, …).  
Figures: `results/genome/figures/`.

## Key scripts (reference)

| Script | Purpose |
|--------|---------|
| `scripts/protein/CSV.py` | Parse FASTA → amino-acid composition CSV |
| `scripts/protein/plot.py` | Scatter, linear regression, LOWESS |
| `scripts/protein/pca.py` | PCA with clustering |
| `scripts/genome/dna_csv.py` | Build genome CSV from FASTA |
| `scripts/genome/ratio_1base.py` | Mononucleotide frequencies |
| `scripts/genome/comparison_all.py` | Cross-species 3-base comparison plot |
| `scripts/genome/repeated.py` | Repeated-motif analysis |

## Course context

Laboratory course on scripting for bioinformatics: public databases, FASTA/CSV formats, descriptive statistics, and visualization. A third module (NCBI taxonomy — eukaryotic lineages, clades with ≥10,000 species) was part of the syllabus but is not included in this repository.

## License

Academic / portfolio use. Follow [NCBI data usage policies](https://www.ncbi.nlm.nih.gov/home/about/policies/) when redownloading or sharing sequence data.

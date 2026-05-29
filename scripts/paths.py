"""Repository path constants for analysis scripts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Raw inputs (FASTA; not tracked in git)
RAW = ROOT / "data" / "raw"
RAW_PROTEIN = RAW / "protein"
RAW_GENOME = RAW / "genome"

# Processed tables
PROTEIN_CSV = ROOT / "data" / "processed" / "protein"
GENOME_CSV = ROOT / "data" / "processed" / "genome"

# Protein outputs
PROTEIN_FIGURES = ROOT / "results" / "protein" / "figures"
PROTEIN_PLOTS = ROOT / "results" / "protein" / "plots"

# Genome outputs
GENOME_FIGURES = ROOT / "results" / "genome" / "figures"
GENOME_TABLES = ROOT / "results" / "genome" / "tables"
GENOME_SPECIES = ROOT / "results" / "genome" / "species"

# Genome table subdirectories
GENOME_TABLES_MONO = GENOME_TABLES / "mono_nucleotide"
GENOME_TABLES_DI = GENOME_TABLES / "dinucleotide"
GENOME_TABLES_TRI = GENOME_TABLES / "trinucleotide"
GENOME_TABLES_CHR_LEN = GENOME_TABLES / "chromosome_length"
GENOME_TABLES_CHR_RATIO = GENOME_TABLES / "chromosome_ratio"
GENOME_TABLES_REPEATED = GENOME_TABLES / "repeated"


def ensure_dirs() -> None:
    """Create standard data and result directories if missing."""
    for path in (
        RAW_PROTEIN,
        RAW_GENOME,
        PROTEIN_CSV,
        GENOME_CSV,
        PROTEIN_FIGURES,
        PROTEIN_PLOTS,
        GENOME_FIGURES,
        GENOME_TABLES,
        GENOME_SPECIES,
        GENOME_TABLES_MONO,
        GENOME_TABLES_DI,
        GENOME_TABLES_TRI,
        GENOME_TABLES_CHR_LEN,
        GENOME_TABLES_CHR_RATIO,
        GENOME_TABLES_REPEATED,
    ):
        path.mkdir(parents=True, exist_ok=True)

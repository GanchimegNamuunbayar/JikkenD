import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1]))
from paths import (
    GENOME_CSV,
    GENOME_FIGURES,
    GENOME_SPECIES,
    GENOME_TABLES,
    GENOME_TABLES_CHR_LEN,
    GENOME_TABLES_CHR_RATIO,
    GENOME_TABLES_DI,
    GENOME_TABLES_MONO,
    GENOME_TABLES_REPEATED,
    GENOME_TABLES_TRI,
    RAW_GENOME,
)

import os

def write_fasta_headers_to_file(input_file_path, output_file_path):
    # 出力ファイルのディレクトリを取得
    output_dir = os.path.dirname(output_file_path)
    
    # ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)
    
    # 入力ファイルを読み込み、出力ファイルに書き出す
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            if line.startswith('>'):
                output_file.write(line)

# 入力ファイルと出力ファイルのパスを指定
input_file_path = RAW_GENOME / "Musculus2/GCA_030265425.1_NEI_Mmus_1.0_genomic.fna"
output_file_path = GENOME_SPECIES / "Musculus/genomic_fna_headers2.txt"

# 関数を呼び出してヘッダー行を書き出す
write_fasta_headers_to_file(input_file_path, output_file_path)

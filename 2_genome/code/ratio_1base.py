import pandas as pd
import os
import glob
from collections import Counter

def count_chr1_nucleotides(df):
    chr1_frequency = Counter()
    # Convert Chromosome column to numeric, ignoring errors
    df['Chromosome'] = pd.to_numeric(df['Chromosome'], errors='coerce')
    chr1_df = df[df['Chromosome'] == 1]

    for _, row in chr1_df.iterrows():
        # Count each base in the sequence, ignoring 'N'
        for base in row['Sequence']:
            if base != 'N':
                chr1_frequency[base] += 1
    
    return chr1_frequency


csv_file = "../csv/Chlamydomonas.csv"

df = pd.read_csv(csv_file)

chr1_frequency = count_chr1_nucleotides(df)
total_bases = sum(chr1_frequency.values())
base_ratios = {base: chr1_frequency[base] / total_bases for base in 'ATGC'}
results_df = pd.DataFrame(base_ratios.items(), columns=['Base', 'Ratio'])

excel_output_path = '../output/Chlamydomonas/1base_ratio.xlsx'
results_df.to_excel(excel_output_path, index=False)

print(f"Results have been saved to {excel_output_path}")


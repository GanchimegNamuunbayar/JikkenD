import csv

def read_fasta_file(file_path):
    chromosomes = {}
    current_chromosome = 1  # Initialize the chromosome number
    current_sequence = ""

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>NC'):
                if current_sequence:
                    chromosomes[current_chromosome] = current_sequence.upper()  # Convert sequence to uppercase
                    current_chromosome += 1  # Increment the chromosome number
                current_sequence = ""
            else:
                current_sequence += line.strip()
        chromosomes[current_chromosome] = current_sequence.upper()  # Convert sequence to uppercase
        if 20 in chromosomes:
            chromosomes['X'] = chromosomes.pop(23)
        if 21 in chromosomes:
            chromosomes['Y'] = chromosomes.pop(24)
    return chromosomes


def save_to_csv(chromosomes, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Chromosome', 'Sequence'])
        for chromosome, sequence in chromosomes.items():
            writer.writerow([chromosome, sequence])  # Convert chromosome number

# 使用例
file_path = '..//dataset/Homosapiens2/GCF_009914755.1_T2T-CHM13v2.0_genomic.fna'
output_csv = '../csv/Homosapiens.csv'
chromosomes = read_fasta_file(file_path)

# 最初の染色体と最後のXとYの染色体だけを抽出
#selected_chromosomes = {1: chromosomes[1], 5: chromosomes[5], 10: chromosomes[10], 15: chromosomes[15], 19: chromosomes[19], 'X': chromosomes['X'], 'Y': chromosomes['Y']}

save_to_csv(chromosomes, output_csv)

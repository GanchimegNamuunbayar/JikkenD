import csv

def read_fasta_file(file_path):
    chromosomes = {}
    current_chromosome = 1  # Initialize the chromosome number
    current_sequence = ""

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>CM'):
                if current_sequence:
                    chromosomes[current_chromosome] = current_sequence.upper()  # Convert sequence to uppercase
                    current_chromosome += 1  # Increment the chromosome number
                current_sequence = ""
            else:
                current_sequence += line.strip()
        chromosomes[current_chromosome] = current_sequence.upper()  # Convert sequence to uppercase
        if 20 in chromosomes:
            chromosomes['X'] = chromosomes.pop(20)
        if 21 in chromosomes:
            chromosomes['Y'] = chromosomes.pop(21)
    return chromosomes


def save_to_csv(chromosomes, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Chromosome', 'Sequence'])
        for chromosome, sequence in chromosomes.items():
            writer.writerow([chromosome, sequence])  # Convert chromosome number

# 使用例
file_path = '../dataset/Musculus2/GCA_030265425.1_NEI_Mmus_1.0_genomic.fna'
output_csv = '../csv/Musculus.csv'
chromosomes = read_fasta_file(file_path)
save_to_csv(chromosomes, output_csv)

from Bio import SeqIO
import matplotlib.pyplot as plt
import seaborn as sns

# fastaファイルの読み込み
fasta_file = "protein.faa"

# タンパク質の長さのリストを初期化
protein_lengths = []

# fastaファイルからタンパク質の長さを取得
for record in SeqIO.parse(fasta_file, "fasta"):
    protein_lengths.append(len(record.seq))

# 密度分布のプロット
sns.displot(protein_lengths, kde=True)
plt.title('Protein Length Density Distribution (Saccharomyces cerevisiae)')
plt.xlabel('Protein Length')
plt.ylabel('Density')
plt.show()

# 箱ひげ図のプロット
sns.boxplot(y=protein_lengths)
plt.title('Boxplot of Protein Lengths (Saccharomyces cerevisiae)')
plt.ylabel('Protein Length')
plt.show()

# バイオリンプロットのプロット
sns.violinplot(y=protein_lengths)
plt.title('Violin Plot of Protein Lengths (Saccharomyces cerevisiae)')
plt.ylabel('Protein Length')
plt.show()

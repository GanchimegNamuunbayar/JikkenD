import pandas as pd
import matplotlib.pyplot as plt

# Define paths to your Excel files
excel_output_paths = [
    '../output/Thaliana/chromosome_lengths.xlsx',
    '../output/Chlamydomonas/chromosome_lengths.xlsx',
    '../output/Cyanidioschyzon/chromosome_lengths.xlsx',
    '../output/Homosapiens/chromosome_lengths.xlsx',
    '../output/Musculus/chromosome_lengths.xlsx',
    '../output/Rerio/chromosome_lengths.xlsx',
    '../output/Saccharomyces/chromosome_lengths.xlsx',
]

# Set up the main figure and subplots
fig, axes = plt.subplots(nrows=len(excel_output_paths), ncols=1, figsize=(8, 10), sharex=True)

# Iterate over each Excel file
for idx, excel_output_path in enumerate(excel_output_paths):
    # Load data from Excel
    df = pd.read_excel(excel_output_path)

    # Boxplot
    axes[idx].boxplot(df['GenomeLength'], patch_artist=False, vert=False, positions=[0], widths=0.6, showfliers=False)

    # Scatter plot with chromosome numbers
    for index, row in df.iterrows():
        axes[idx].scatter(row['GenomeLength'], 0, marker='o', color='red')
        #axes[idx].text(row['GenomeLength'], 0.05, row['Chromosome'], 
                       #verticalalignment='bottom', horizontalalignment='left', fontsize=10)

    # Customize axes and labels
    axes[idx].set_yticks([0])
    axes[idx].set_yticklabels([excel_output_path.split('/')[2]])  # Extract organism name from path

    # Set x-axis to log scale
    axes[idx].set_xscale('log')

    # Enable grid
    axes[idx].grid(True)

# Labeling and title for the x-axis
axes[-1].set_xlabel('Ghromosome Length (log scale)')

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('../output/all_plots_vertical_logscale.png')

# Display the plot
plt.show()

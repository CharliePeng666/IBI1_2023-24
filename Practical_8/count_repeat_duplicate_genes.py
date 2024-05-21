import re
from Bio import SeqIO

repeat_seq = input("Enter the repetitive sequence ('GTGTGT' or 'GTCTGT'): ")

input_file = 'c:\Users\彭成远\Desktop\IBI\IBI1_2023-24\Practical_8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = f'{repeat_seq}_duplicate_genes.fa'

duplicate_genes_with_repeats = {}
for record in SeqIO.parse(input_file, "fasta"):
    if re.search(repeat_seq, str(record.seq)):
        simplified_name = record.id.split('|')[0] 
        duplicate_genes_with_repeats[simplified_name] = str(record.seq)
with open(output_file, 'w') as output_handle:
    for gene_name, gene_sequence in duplicate_genes_with_repeats.items():
        output_handle.write(f">{gene_name}\n{gene_sequence}\n")
from Bio import SeqIO
input_file = 'c:\Users\彭成远\Desktop\IBI\IBI1_2023-24\Practical_8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'duplicate_genes.fa'
duplicate_genes = {}

for record in SeqIO.parse(input_file, "fasta"):
    if 'duplication' in record.description:
        simplified_name = record.id.split('|')[0]
        duplicate_genes[simplified_name] = str(record.seq)
with open(output_file, 'w') as output_handle:
    for gene_name, gene_sequence in duplicate_genes.items():
        output_handle.write(f">{gene_name}\n{gene_sequence}\n")
    
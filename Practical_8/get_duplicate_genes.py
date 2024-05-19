
from Bio import SeqIO

def extract_genes_with_duplication(fasta_file):
    duplicated_genes = {}
    for record in SeqIO.parse(fasta_file, "fasta"):
        if 'duplication' in record.description:
            simplified_name = record.description.split()[0]
            duplicated_genes[simplified_name] = str(record.seq)
    return duplicated_genes

def write_fasta(duplicate_genes, output_file):
    SeqIO.write(duplicate_genes.values(), output_file, "fasta")

duplicated_genes = extract_genes_with_duplication("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")

write_fasta(duplicated_genes, "duplicate_genes.fa")

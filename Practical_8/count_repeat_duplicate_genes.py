from Bio import SeqIO

def count_repeats(sequence, pattern):
    return sequence.count(pattern)

def filter_genes_with_repeat(duplicate_genes, repeat_pattern):
    filtered_genes = {}
    for gene_name, sequence in duplicate_genes.items():
        if count_repeats(sequence, repeat_pattern) > 0:
            filtered_genes[gene_name] = sequence
    return filtered_genes

def write_fasta_with_repeats(duplicate_genes, repeat_pattern, output_file):
    for record in SeqIO.parse(duplicate_genes, "fasta"):
        if repeat_pattern in str(record.seq):
            new_name = f"{record.id}_{count_repeats(str(record.seq), repeat_pattern)}"
            new_record = record.__class__(seq=record.seq, id=new_name, description="")
            SeqIO.write(new_record, output_file, "fasta")

duplicate_genes = SeqIO.to_dict(SeqIO.parse("duplicate_genes.fa", "fasta"))

repeat_pattern = input("Enter the repetitive sequence ('GTGTGT' or 'GTCTGT'): ")

filtered_genes = filter_genes_with_repeat(duplicate_genes, repeat_pattern)

output_filename = f"{repeat_pattern}_duplicate_genes.fa"
write_fasta_with_repeats(filtered_genes, repeat_pattern, output_filename)
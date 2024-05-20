def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('>'):
                gene_name = line[1:].strip().split()[0]
                sequences[gene_name] = []
            else:
                sequences[gene_name].append(line.strip())
    return sequences

def filter_by_duplication(sequences):
    duplicated_genes = {name: ''.join(seqs) for name, seqs in sequences.items() if 'duplication' in name}
    return duplicated_genes

def write_fasta(sequences, output_file):
    with open(output_file, 'w') as file:
        for name, sequence in sequences.items():
            file.write(f">{name}\n")
            file.write(f"{sequence}\n")

FAsta = 'c:\Users\彭成远\Desktop\IBI\IBI1_2023-24\Practical_8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
sequences = read_fasta(FAsta)

duplicated_genes = filter_by_duplication(sequences)

write_fasta(duplicated_genes, 'duplicate_genes.fa')
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'

def count_repeats(sequence, pattern):
    count = 0
    start = 0
    while start < len(sequence):
        start = sequence.find(pattern, start)
        if start + len(pattern) > len(sequence):
            break
        if start != -1:
            count += 1
            start += len(pattern)
        else:
            break
    return count

gtgtgt_count = count_repeats(seq, 'GTGTGT')
gtctgt_count = count_repeats(seq, 'GTCTGT')

print(f"Total 'GTGTGT' repeats: {gtgtgt_count}")
print(f"Total 'GTCTGT' repeats: {gtctgt_count}")
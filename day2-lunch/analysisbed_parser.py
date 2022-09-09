import extendbed_parser
bed = extendbed_parser.parse_bed('hg38_gencodev41_chr21.bed')
print(bed)

# ['chr21', 46690763, 46691226, 'ENST00000427757.1', 0.0, '+', 46690763, 46690763, '255,51,255', 1, '463,', '0,']]

 # output from bed parser # [[chr21, 50, 53][]]
 # need to get out the 10th thing, and create a new list of exon #s, then get the median 
 # to get the median 1. sort, 2. index list based on length of the list // 2 
exons = []

for i, line in enumerate(bed):
    for j in line:
        num_exon = line[9]
        exons.append(num_exon)
    exons.sort()
    mid = len(exons) // 2
    med = (exons[mid] + exons[~mid]) / 2
print(med)
Assignment 1: Genome Assembly

Question 1-

1.1 How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?/
1,000,000 *5 = 500000/100= 50,000 -100bp reads
1,000,000 *15 = 15000000/100= 150,000 -100bp reads

1.2 code in simreads.py

1.3 7123 --> bp that has not been sequenced

----
Question 2-
code ran, downloaded spades:

~/SPAdes-3.15.5-Darwin/bin/spades.py --pe-1 1 ./frag180.1.fq copy --pe-2 2 ./frag180.2.fq copy --mp-1 1 ./jump2k.1.fq copy --mp-2 2 jump2k.2.fq copy -t 4 -k 31 -o asm

2.1 4;grep -c '>' contigs.fasta; samtools faidx contigs.fasta

2.2 want to index each contig, seperate heaer, get length of sequence by samtools -n ; 105830 + 47860 + 41351 + 39426; awk '{sum+=$2} END {print sum}' "contigs.fasta.fai"
2.3 105830; cut -f2 contigs.fasta.fai | sort -n -r | head -1
2.4 total of number divided by the smallest amount: 117, 233.5


----

Question 3-

3.1 AvgIdentity =  99.9823              99.9823
3.2 116896.0000 
3.3 1 insertions, 2 deletions

----

Question 4- 

4.1 26787 between 27500

4.2 713

4.3 
">NODE_1_length_234497_cov_20.506978:26787-27500
CCGCCCATGCGTAGGGGCTTCTTTAATTACTTGATTGACGCATGCCCCTCGTTCTACATG
TCTAGCTTCGTAACTGCCCCGATTTATACAGGAGCATATGCGTTTCGTAGTGCCGGGAAT
GCATACCAAAGGGCTCACGGCGGGTACGCCACAATGGCTCAAGTCGAAAATGAATCGAAG
ACAACAAGGAATACCGTACCCAATTACTCAAGGACCTCATACACCATCCCATGCTACTTA
TCTACAGACATACACGCCAGCACCCAGCAACCAAAGCACACCGACGATAAGACTACAATC
GCGATAAGCACAACTTACATTAGGAGGCCCGGCAAATCTTGACGGCGTTAAGTCCGACAC
GAATACCCCCCGACAAAAGCCTCGTATTCCGAGAGTACGAGAGTGCACAAAGCACCAAGG
CGGGGCTTCGGTACATCCACCAGTAGTCCCGTCGTGGCGGATTTTCGTCGCGGATGATCC
GAGGATTTCCTGCCTTGCCGAACACCTTACGTCATTCGGGGATGTCATAAAGCCAAACTT
AGGCAAGTAGAAGATGGAGCACGGTCTAAAGGATTAAAGTCCTCGAATAACAAAGGACTG
GAGTGCCTCAGGCATCTCTGCCGATCTGATTGCAAGAAAAAATGACAATATTAGTAAATT
AGCCTATGAATAGCGGCTTTAAGTTAATGCCGAGGTCAATATTGACATCGGTAG"

4.4 
python asm/dna-decode.py -d --input dnamsg1.fasta
samtools faidx scaffolds.fasta NODE_1_length_234497_cov_20.506978:26788-27499 > dnamsg1.fasta
Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens...








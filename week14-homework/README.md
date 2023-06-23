#Step 1
To get pie charts of 1st day --> ktImportText SRR4921.._krona.text -q --> open text.krona.html

Question 1:
Trends I notice of the microbiotata in the frist week is that there isn't much diversity of the biomes. Enterococcus faecalis is the most abundant bacteria in the Bacilli group which is found in the body by way of ingestion of foods, orignally being found in soil. Staphylococcus epidermis is the most abundant in the Bacillales group which is found on the surface of the skin. Other bacteria in each group were found in trace amounts (>10%).

to add the links just use git add html

#Step 2
Question 2: The metrics of the contigs that could be used to group them together is the overlapping read converage or how many times reads have been found 

2A:  
bwa index metagenomics_data/step0_givendata/assembly.fasta
 
2B:
bwa mem -t 4 metagenomics_data/step0_givendata/assembly.fasta metagenomics_data/step0_givendata/READS/SRR492197_1.fastq metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.sam

samtools sort -o rSR492197.bam SRR492197.sam
samtools sort -o rSR492194.bam SRR492194.sam
samtools sort -o rSR492193.bam SRR492193.sam
samtools sort -o rSR492190.bam SRR492190.sam
samtools sort -o rSR492189.bam SRR492189.sam
samtools sort -o rSR492188.bam SRR492188.sam
samtools sort -o rSR492186.bam SRR492186.sam
samtools sort -o rSR492183.bam SRR492183.sam

2D:
jgi_summarize_bam_contig_depths --outputDepth depth.txt *.bam

metabat2 -i assembly.fasta -a depth.txt -o bins_dir/bin

Question 3A: 6 bins 
Question 3B: 4% of binned contigs, does not take into account of the sequence length of the unbinned
grep -c '>' metagenomics_data/step0_givendata/assembly.fasta, 4103 total contigs
grep -c '>' bins_dir/bin.*.fa, 55+78+8+37+13+6 = 197 contigs in bins 

Question 3C: 
grep -v '>' bins_dir/bin.*.fa | wc -l
219884 -> lines of sequence 

grep -v '>' bins_dir/bin.1.fa | wc -c

bin1- 2,750,133 
bin2- 2,289,418
bin3- 1,683,638
bin4- 1,248,387
bin5- 2,525,062
bin6- 2,910,568

length of prokary is 5MB--> 5 million base pairs
This coverage is pretty good, from making contigs from smaller reads. 

Question 3D:
use known genomes to map back bins, fiter out the species that isnt supposed to be there. 

#Step 4
 
grep '>' bins_dir/bin.1.fa | tr -d ">" > bin1.txt 
grep '>' bins_dir/bin.2.fa | tr -d ">" > bin2.txt 
grep '>' bins_dir/bin.3.fa | tr -d ">" > bin3.txt 
grep '>' bins_dir/bin.4.fa | tr -d ">" > bin4.txt 
grep '>' bins_dir/bin.5.fa | tr -d ">" > bin5.txt 
grep '>' bins_dir/bin.6.fa | tr -d ">" > bin6.txt

grep -f bin1.txt metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin1species.txt-Stap
grep -f bin2.txt metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin2species.txt
grep -f bin3.txt metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin3species.txt
grep -f bin4.txt metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin4species.txt
grep -f bin5.txt metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin5species.txt
grep -f bin6.txt metagenomics_data/step0_givendata/KRAKEN/assembly.kraken > bin6species.txt

Question 4A:
bin1 - Staphylococcus aureus
bin2 - Staphylococcus epidermidis, aureus
bin3 - Anaerococcus prevotii, Streptococcus anginosus,Finegoldia magna,Clostridium 
bin4 - Staphylococcus haemolyticus
bin5 - Cutibacterium avidum
bin6 - Enterococcus faecalis

Question 4B:
parse through the indexes for the bacteria species, then count how many of those there are in one contig. 


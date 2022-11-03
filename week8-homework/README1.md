#QBB Week 8
part 1: code:

chr11:1900000-2800000
chr14:100700000-100990000
chr15:23600000-25900000
chr20:58800000-58912000

medaka_variant -f hg38.fa -i methylation.bam -r chr11:1900000-2800000 -o chr11 -p 
medaka_variant -f hg38.fa -i methylation.bam -r chr14:100700000-100990000 -o chr14 -p
medaka_variant -f hg38.fa -i methylation.bam -r chr15:23600000-25900000 -o chr15 -p
medaka_variant -f hg38.fa -i methylation.bam -r chr20:58800000-58912000 -o chr20 -p 

part 2: code
chr 11 : ~/qbb2022-answers/week8-homework/chr11/round_0_hap_mixed_phased.vcf.gz 
chr 14 : ~/qbb2022-answers/week8-homework/chr14/round_0_hap_mixed_phased.vcf.gz	
chr 15 : ~/qbb2022-answers/week8-homework/chr15/round_0_hap_mixed_phased.vcf.gz
chr 20 : ~/qbb2022-answers/week8-homework/chr20/round_0_hap_mixed_phased.vcf.gz

whatshap haplotag -o chr11.bam --reference hg38.fa ~/qbb2022-answers/week8-homework/chr11/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr11.tsv
whatshap haplotag -o chr14.bam --reference hg38.fa ~/qbb2022-answers/week8-homework/chr14/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr14.tsv
whatshap haplotag -o chr15.bam --reference hg38.fa ~/qbb2022-answers/week8-homework/chr15/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr15.tsv
whatshap haplotag -o chr20.bam --reference hg38.fa ~/qbb2022-answers/week8-homework/chr20/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr20.tsv

did samtools index for each one for the next step:
samtools index chr11.bam
samtools index chr14.bam
samtools index chr15.bam
samtools index chr20.bam

part 3: codes
whatshap split --output-h1 chr11_h_1.bam --output-h2 chr11_h_2.bam chr11.bam chr11.tsv
whatshap split --output-h1 chr14_h_1.bam --output-h2 chr14_h_2.bam chr14.bam chr14.tsv
whatshap split --output-h1 chr15_h_1.bam --output-h2 chr15_h_2.bam chr15.bam chr15.tsv
whatshap split --output-h1 chr20_h_1.bam --output-h2 chr20_h_2.bam chr20.bam chr20.tsv

samtools cat chr11_h_1.bam chr14_h_1.bam chr15_h_1.bam chr20_h_1.bam > regions_h1.bam
samtools cat chr11_h_2.bam chr14_h_2.bam chr15_h_2.bam chr20_h_2.bam > regions_h2.bam

part 4: codes are in the assignment, 

part 5: codes are in the assignment, 

part 6: answer
Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning.
yes, ...
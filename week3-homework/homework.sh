## These are the lines for step 1-2
#for i in A01_35.fastq A01_31.fastq A01_27.fastq A01_24.fastq A01_23.fastq A01_11.fastq A01_09.fastq	A01_39.fastq A01_62.fastq A01_63.fastq
# do
# 	bwa mem -R "@RG\tID:${i}\tSM:${i}" sacCer3.fa $i > ${i}.sam
# 	echo $i
# done

# for i in A01_35.fastq.sam.bam A01_31.fastq.sam.bam A01_27.fastq.sam.bam A01_24.fastq.sam.bam A01_23.fastq.sam.bam A01_11.fastq.sam.bam A01_09.fastq.sam.bam	A01_39.fastq.sam.bam \
# A01_62.fastq.sam.bam A01_63.fastq.sam.bam
# do
# 	samtools index -b $i
# done

## These are the lines of code for 3-7
# freebayes -f sacCer3.fa -p 1 --genotype-qualities *.bam > variants.vcf 

# vcffilter -f "QUAL > 20" variants.vcf > fvariants.vcf

# vcfallelicprimitives -k -g fvariants.vcf > dvariants.vcf

# snpeff ann R64-1-1.99 dvariants.vcf > test.vcf

#just notes (dont pay attention) cmds : pass, break, continue 



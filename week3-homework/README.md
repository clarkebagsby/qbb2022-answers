#Week 3-Homework

#Step 1
```
bwa index sacCer.fa
```

#Step 2
```
for i in A01_35.fastq A01_31.fastq A01_27.fastq A01_24.fastq A01_23.fastq A01_11.fastq A01_09.fastq	A01_39.fastq A01_62.fastq A01_63.fastq
do
	bwa mem -R "@RG\tID:$i\tSM:$i" -t 12 -o $i.sam sacCer3.fa $i 
done
```
#Step 3a
```
for i in A01_35.fastq A01_31.fastq A01_27.fastq A01_24.fastq A01_23.fastq A01_11.fastq A01_09.fastq	A01_39.fastq A01_62.fastq A01_63.fastq
do
	samtools sort -o $i.bam $i.sam
done
```

#Step 3b
```
for i in A01_35.fastq.sam.bam A01_31.fastq.sam.bam A01_27.fastq.sam.bam A01_24.fastq.sam.bam A01_23.fastq.sam.bam A01_11.fastq.sam.bam A01_09.fastq.sam.bam	A01_39.fastq.sam.bam \
 A01_62.fastq.sam.bam A01_63.fastq.sam.bam
 do
 	samtools index -b $i
 done
```
#Step 4
```
freebayes -f sacCer3.fa -p 1 --genotype-qualities *.bam > variants.vcf 
```
#Step 5
```
vcffilter -f "QUAL > 20" variants.vcf > fvariants.vcf
```
#Step 6
```
vcfallelicprimitives -k -g fvariants.vcf > dvariants.vcf
```
#Step 7
```
snpeff ann R64-1-1.99 dvariants.vcf > test.vcf
```



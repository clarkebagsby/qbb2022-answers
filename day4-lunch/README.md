#QBB-Day 4-Lunch Exercises

Exercise 1:

1. The output that reports how many bp features covers is in the png images created following the line of code that converts each column in the GTF file into a vcf file
2. A way to compare the images is to convert the image into a numpy.array then compare the lists of the binary values converted from the picture.
3. lncRNA, unproccesed_pseudogene_, transcribed_proceesed_pseudogene : I am interested in why you would want to know more about the unproccessed_pseudogene_ since it tells introns and regulatory sequences

Exercise 2:
3. code below!

#!/bin/bash

GTF=$1
CHR=chr21

if [ ! -f $CHR.gtf ]
then
    echo "--- Creating $CHR.gtf"
    grep -w $CHR $GTF > $CHR.gtf
fi

for TYPE in lncRNA
do
    echo "--- Creating $TYPE.$CHR.bed"
    grep $TYPE $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="gene"){print $1, $4-1, $5}}' > $TYPE.$CHR.bed
done

echo "--- Creating exons.$CHR.bed"
grep "lncRNA" $CHR.gtf | awk 'BEGIN {OFS="\t"}{if ($3=="exon"){print $1, $4-1, $5}}' > exons.$CHR.bed
---

graphs have been uploaded to github
--- 

trends noticed are there is uneven distributioon of the exons --> showing how some parts of the exon might not be BP regiion
							even dist. of processed_pseudogenes_ --> sgenetiic variability of the gene read in that region
							right-skewed for lncRNA --> suggesting low allels there 
---
Exercise 3:
 SYNOPSIS
     bxlab/cmdb-plot-vcfs -- [file1] [file2]

 USAGE
     bash do_all.sh <vcf_file> <gtf_file> ...

     <file>   need to file in a vcf and gtf

 DESCRIPTION
     1. Create .bed files for features of interest
         - Run subset_regions.sh Bash script on GTF file
         - Use grep to find the length of BP overlap between the VCF and the bed of GTF file
	 2. vcf file is changed for feature of interest based upon whats in .bed()
	 	 - bedtools sort & merge of the .bed() file 
		 - create new vcf with new feature of intrest
	 3. Plot the feature of interest with values from .vcf
	     - Run python plot_vcf_ac.py on feature


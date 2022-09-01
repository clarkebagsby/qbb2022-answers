# QBB2022 - Day 1 - Homework Exercises Submission
Exercise 1:

A. error message was `awk illegal field`

B. output = 
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
 
Transition tranversion- yes, A is purine but matches structure of G so it makes sense that there are more G substitutions for A. 

Exercise 2:
What’s the most common alternate allele for a Cytosine reference allele for variants occurring in promoter like regions of the genome?-->find stacks associ. w/promoter region

Active TSS-1,2, bivalent TSS-10,11
 olution-make bed file with those two states
solution-intersect variant file with file of interest chr

awk ' {if ($4 == 1 || $4 == 2 || $4 == 10 || $4 == 11) {print}}'  ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promoters.bed

 bedtools intersect -a ~/data/vcf_files/random_snippet.vcf -b~/qbb2022-answers/day1-homework/promoters.bed > intersect.vcf

./exercise1.sh intersect.vcf
output=
Considering  A
   6 C
  32 G
   8 T
Considering  C
  12 A
  11 G
  39 T
Considering  G
  46 A
  17 C
  11 T
Considering  T
  10 A
  29 C
   8 G


Exercise 3:
line 1 is converting a vcf file into a bed with chromosome name, position - 1, and set # into variable to variants.bed
line 2 is sorting the new file genes.bed by chromosome and position number
line 3 is takiing variants and looking into genes.sorted.bed for those variants and all those nearest to those genes selected

Error: 
unable to open file or unable to determine types for file variants.bed

- Please ensure that your file is TAB delimited (e.g., cat -t FILE).
- Also ensure that your file has integer chromosome coordinates in the 
  expected columns (e.g., cols 2 and 3 for BED).
  
-solution: add a tab delimitter("\t") at start of awk command.
-solution: add a line that sorts the variants.bed 
  
How many variants are returned and how many unique genes are returned? How many variants on average are therefore connected to a gene with bedtools closest?

10293 variants
200 genes

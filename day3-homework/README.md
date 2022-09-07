# QBB2022 - Day 3 - Homework Exercises Submission

# Exercise 1:
The code to run plink using --pca is:
plink --vcf /Users/cmdb/data/vcf_files/ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca 3

# Exercise 2:
for plot A (above) has negative distribution while plot B (below) has a positive distribution, each being centralized around 1.

#Exercise 3:
tail -n +2 integrated_call_samples.panel | sort -k 1 > try2.txt
awk 'BEGIN{OFS="\t"} {$1=$1; print}' plink.eigenvec | sort -k 1 > sorted_eigenvec
join -1 1 -2 1 sorted_eigenvec try2.txt
 

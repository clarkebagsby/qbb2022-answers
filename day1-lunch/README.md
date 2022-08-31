# QBB2022 - Day 1 - Lunch Exercises Submission
1. I am excited to learn better methods for remembering syntax and how to read program languuages for what we are looking for. 
2b. 62.34246, wc -l exons.chr21.bed -->  13653, wc -l genes.chr21.bed --> 219, 13653/219 = 62.34246
2c. to find the median  you would need to find matching positions on the genes and exon files
3b. 15, cut -f 4 chromHMM.E116_15_coreMARKs_hg38lift_stateno.chr21.bed | sort  -n | uniq -c
3c. you would take the positions (start/end) and take the difference. The total from the last can be used to make a percentage between the states and how long the state is.
4b. 123-ACB,, 112-ASW, 173-ESN, 180 GWD, 122--LWK, 128-MSL, 206-YRI, grep AFR integrated_call_samples.panel | cut -f 2 | sort | uniq -c
4c. search for poppulation, cut to just that list of pop., sort them, then filter
5. pull ouut HG00100
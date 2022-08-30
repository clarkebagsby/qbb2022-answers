#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk '/^#/{next} BEGIN{OFS="\t"} {print $1,$2-1, $2}' $1 > variants.bed  #fixes tab in random_snippet 

sort -k1,1 -k2,2n variants.bed > variants.sorted.bed #adds a sorted variants bed to be used for bedtools closest
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed #stays the same

bedtools closest -a variants.sorted.bed -b genes.sorted.bed #prints variants for each gene at different chromosome #'s 





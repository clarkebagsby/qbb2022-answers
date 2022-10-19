#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

## code for creating plot of PC1 and PC2


#
sorted_data = np.genfromtxt("plink.eigenvec", dtype = None, encoding = None, names = ["sampleID", "sample2ID", "PC1", "PC2", "PC3", "PC4", "PC5", "PC6", "PC7","PC8", "PC9", "PC10"])
maf = np.genfromtxt("plink.frq", dtype = None, encoding = None, skip_header = 1, names = ["CHR", "SNP", "A1", "A2", "MAF", "NCHROBS"])

#question 2

# fig, ax = plt.subplots()
# ax.scatter(sorted_data["PC1"], sorted_data["PC2"])
# ax.set_xlabel("PC1")
# ax.set_ylabel("PC2")
# ax.set_title("Principle Component Analysis of Genetypes of Cell Lines") #add title and legend
# plt.savefig("ex4_a.png")
# plt.close(fig)

#question 3

# fig, ax = plt.subplots()
# ax.hist(maf["MAF"])
# ax.set_xlabel("PC1")
# ax.set_ylabel("frequencies")
# ax.set_title("Minor Allele Frequencies ") #add title and legend
# plt.savefig("ex4_b.png")


# question 5
# lin_assoc = open("final_results_test.assoc.linear", 'r')
# count = 0
# count_list = []
# log10_p_values= []
# colors = []
# pvalt = 1e-5
#
# for i, line in enumerate(lin_assoc):
#     if i == 0:
#         continue
#     pval = float(line.split()[8])
#     log10_p_values.append(np.log10(pval)* -1)
#     # print(np.log10(float(line.split()[8]))*-1)
#     count += 1
#     count_list.append(count)
#     if pval < pvalt:
#         colors.append('red')
#     elif pval > pvalt:
#         colors.append('blue')
#     else:
#         colors.append('purple')
#
#
# fig, ax = plt.subplots()
# ax.scatter(count_list, log10_p_values, c = colors)
# ax.set_xlabel("chromosome")
# ax.set_ylabel("log10 p values")
# plt.savefig("ex4_c.png")
# plt.close()
# 
#
# #question 6 : take from genotype.vcf and CB... file
#
# linear = open("final_results_test.assoc.linear", 'r')
# genotypes = open('genotypes.vcf', 'r')
# pval =[]
# snp = []
# for line in linear:
#     if line == 0:
#         continue
#     line = line.split()
#     if line[4] == "ADD":
#        pval.append(float(line[8]))
#        snp.append(line[1])
# low_pval = min(pval)
# index_p = pval.index(low_pval) # gets the associated p val
# assoc_snp = snp[index_p] # gets the associated snp
#
# # match the snp to genotype file
# # in genotype, need to match the SNP ID to the line in ID and pull out the genotype data(the )
# # dictionary 1, from genotypes, key= individual, value = genotype info (0/0)
# # search through phenotypes by the individual #, by keys, then get the value for phenotype and put into list
# # graph: x-axis will have the different genotypes(0/0,0/1,1/1) y axis will have
#
# id_genotype = {}
# indviduals = []
# homogenous =[] #1/1
# heterozygous = [] #0/1
# zero = [] #
# for line in genotypes:
#     if line.startswith('##'):
#         continue
#     line2 = line.split()
#     if line2[0] == '#CHROM':
#         for i in line2[9:]:
#             id_genotype[i] = "" #initializing the dictionary with empty string so we could later add in that value
#     act_g = line2[9:] #['1/1', '0/1', './.', '0/0', '0/1', '0/1', '0/1',
#     for i in act_g:
#         id_genotype[i] += act_g
# print(id_genotype)
        
        
## Disregard...       
# id_genotype[i] = act_g


            # id_genotype[i] = line2[9:]
#                 # id_genotype[i] == "0/0"
# #             id_genotype[i] = line3
# #
# print(id_genotype)
   #  id_genotype[i] = genotype_info
# print(id_genotype)
    # if "0/0" in line2:
#         id_genotype[i] = "0/0"
#
#
# print(id_genotype)
#     for
#  #    # if line[2] == assoc_snp:
#  #        id_genotype[line[9:]] = line[9]
# print(id_genotype)



     
    



    














    




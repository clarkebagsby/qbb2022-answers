#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import linkage, leaves_list, dendrogram
from statsmodels.formula.api import ols
from statsmodels.api import qqplot
# from statsmodels.graphics.gofplots import qqplot
from statsmodels.stats.multitest import multipletests



input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names)


rows = input_arr["t_name"] #sample names


fpkm_values = input_arr[col_names[1:]] # this gets the FKPM values in one variable
# print(fpkm_values)

fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=np.float) #creates matrix


median_val = np.median(fpkm_values_2d, axis = 1) #finds median values

filtered_fpkm = fpkm_values_2d[np.where(median_val > 0)[0],:]

extra_filtered_fpkm = np.log2(filtered_fpkm + 0.1) #log transformed
#####

filtered_genes = rows[np.where(median_val > 0)[0]]
#print(filtered_genes[:5])
#print(rows[:5])


gene_cluster = linkage(extra_filtered_fpkm) #clusters based on genes

opp_cluster = np.transpose(extra_filtered_fpkm) # flips the rows and columns

sam_cluster = linkage(opp_cluster) # clusters the samples

test2 = leaves_list(gene_cluster) #list of clustering gene distancce

test5 = leaves_list(sam_cluster) #

extra_filtered_fpkm_organized = extra_filtered_fpkm[:,test5] #reorganizes columns to the list of sorted indexes
extra_filtered_fpkm_organized = extra_filtered_fpkm_organized[test2,:]
plt.imshow(extra_filtered_fpkm_organized, cmap ="plasma", interpolation= "nearest", aspect= "auto")
# plt.setx genes
# plt.sety --> DO THESE CLARKE samples
plt.savefig("wk9_heatmap")
# plt.show()


fig, ax = plt.subplots()
test3  = dendrogram(sam_cluster)
plt.savefig('dendrogram1')
# plt.show() # --> DO THESE CLARKE samples

#make a list of sex and stage from each sample
sexes = []
stages = []

for i in col_names[1:]:
    str_split = i.split('_')
    sexes.append(str_split[0])
    stages.append(str_split[1])

col_names = col_names[1:]

p_values = []
beta_values = []

p_values_sex = []
beta_values_sex = []

for i in range(extra_filtered_fpkm.shape[0]):
    list_of_tuples = []
    for j in range(len(col_names)):
        list_of_tuples.append((filtered_genes[i],extra_filtered_fpkm[i,j], sexes[j], stages[j]))
    longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])

    test1 = ols("fpkm~stage", longdf).fit() #performs model without looking for sex

    test9 = ols("fpkm~stage+sex", longdf).fit() #performs with using sex as coviariate

    p_values.append(test1.pvalues['stage'])
    beta_values.append(test1.params['stage'])

    p_values_sex.append(test9.pvalues['stage'])
    beta_values_sex.append(test9.params['stage'])

arr_p_values = np.array(p_values)
arr_p_values_sex = np.array(p_values_sex)

qqplot(arr_p_values, line='q')
plt.savefig('qqplot for stages')

mut_tests = multipletests(arr_p_values, method='fdr_bh', alpha=0.1) #need to filter the first index



comp_1 = mut_tests[0] #array with the boolean values
arr_comp = np.array(comp_1)
arr_transcripts = np.array(filtered_genes)

print(np.sum(comp_1), flush=True)

# print(comp_1)


diff_exp_trans = arr_transcripts[arr_comp]

print(diff_exp_trans)




idk2 = multipletests(arr_p_values_sex, method= 'fdr_bh')
# print(idk2)

# no qqplot for sex  one

#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.lib.recfunctions as rfn
from scipy.cluster.hierarchy import linkage


input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')

col_names = list(input_arr.dtype.names) 

rows = input_arr["t_name"]

fpkm_values = input_arr[col_names[1:]] # this gets the FKPM values in one variable
# print(fpkm_values)

fpkm_values_2d = rfn.structured_to_unstructured(fpkm_values, dtype=np.float) #creates matrix 
# print(fpkm_values_2d)

median_val = np.median(fpkm_values_2d, axis = 1) #finds median values

filtered_fpkm = fpkm_values_2d[np.where(median_val > 0)[0],:] 

extra_filtered_fpkm = np.log2(filtered_fpkm + 0.1) #log transformed 

cluster1 = np.transpose(extra_filtered_fpkm) # clusters the rows and columns of ex_filt

#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smi
import statsmodels.api as sma
from scipy import stats

comb = np.genfromtxt('parent_age_mut_count.txt', delimiter = " ", dtype = None, encoding = None, names = True)
# print(comb)
# #want to go through each row and pull out:
# # the count of maternal de novo mutations vs. maternal age (upload as ex2_a.png)
# # the count of paternal de novo mutations vs. paternal age (upload as ex2_b.png)
age_m =[]
for index, line in enumerate(comb):
    age_m.append(line[1])#adds the moms age to age_m
#age_m has all the ages of mothers from comb

age_f = []
for index, line in enumerate(comb):
    age_f.append(line[2])#adds the dads age to age_f
#age_f has all the ages of fathers form comb

mut_count_m = []
for index, line in enumerate(comb):
    mut_count_m.append(line[3])#adds the moms mut

mut_count_f = []
for index, line in enumerate(comb):
    mut_count_f.append(line[5])#adds the fathers mut

# #make a graph of these
# fig, ax = plt.subplots()
# x = age_m
# y = mut_count_m
# ax.scatter(x, y, alpha = 0.4, label= "#of muts")
# ax.set_xlabel("age")
# ax.set_ylabel("# of de novo mutants")
# ax.legend()
# plt.savefig('ex2_a.png')
# # ax.hist(age_f, alpha = 0.5, label ='ages of father')
#
#
# fig, ax = plt.subplots()
# x2 = age_f
# y2 = mut_count_f
# ax.scatter(x2, y2, alpha = 0.4, label= "#of muts")
# ax.set_xlabel("age")
# ax.set_ylabel("# of de novo mutants")
# ax.legend()
# # ax.hist(age_f, alpha = 0.5, label ='ages of father')
# plt.savefig('ex2_b.png')

print(stats.ttest_ind(age_m, mut_count_m))
#use smi to test for  maternal age and maternally inherited de novo mutations
# [(154936, 30, 34, 16, 'mother',  36, 'father')] (154936, 30, 34, 16, 'mother',  36, 'father')..]
mom = smi.ols(formula = "age_m ~ mut_count_m + 1", data = comb)
results =  mom.fit()







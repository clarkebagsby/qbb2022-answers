#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt



final = open("test.vcf", "r")

#The read depth distribution of variant genotypes (histogram)
read_depth = []
n_bins = 500

 # all will share the y axis
for line in final:
    if line[0] == "#":
        continue
    line2 = line.split("\t")
# print(line2)
    col_info = line2[7]
# print(col_info)
    genetype_info = col_info.split(";")
    dp = genetype_info[7]
    dp = dp.split(",")
    dp = dp[0] # gives the DP=
    act_dp = dp[3:] # give the number

    read_depth.append(int(act_dp))


final = open("test.vcf", "r")
# # The quality distribution of variant genotypes (histogram)
qual_dist = []
n_bins = 500

for line in final:
    if line[0] == "#":
        continue
    line3 = line.split("\t")
# print(line2)
    col3_info = line3[7]
# print(col_info)
    qual_info = col3_info.split(";")
    qr = qual_info[28]
    qr = qr.split(",")
    qr = qr[0] # gives the DP=
    act_qr = qr[3:] # give the number
    qual_dist.append(int(act_qr))


# The allele frequency spectrum of your identified variants (histogram)
allele_dist = []
n_bins = 500
final = open("test.vcf", "r")
for line in final:
    if line[0] == "#":
        continue
    line4 = line.split("\t")
# print(line2)
    col4_info = line4[7]
# print(col_info)
    allele_info = col4_info.split(";")
    af = allele_info[3]
    af = af.split(",")
    af = af[0] # gives the DP=
    act_af = af[3:] # give the number
    allele_dist.append(float(act_af))


# # A summary of the predicted effect(s) of each variant as determined by snpEff (barplot)
ann_list = {}
n_bins = 500
final = open("test.vcf", "r")
for line in final:
    if line[0] == "#":
        continue
    line4 = line.split("\t")
# print(line4)
    col4_info = line4[7]
# print(col_info)
    ann_info = col4_info.split(";")
    ann2 = ann_info[41]

    ann4 = ann2.split(",")
    ann5 = ann4[0] # gives the ANN=C line
    act_ann = ann5.split('|')
    ann_list.setdefault(act_ann[1], 1) # initializing the dictionary, with on, if key not already there, adds it and adds value of 1, if key is there, then skip, used to keep count, which is why set 1 is used
    ann_list[act_ann[1]] += 1


    # ann_list.append(str(act_ann))
#

#
#

fig, ax = plt.subplots(ncols=2,nrows=2, figsize=(14,10))

ax[0,0].hist(read_depth, bins= n_bins)
ax[0,0].set_xlabel("# of variant gentoypes")
ax[0,0].set_ylabel("frequency of variant genotypes")
ax[0,0].set_title("Distribution of Variant Genotypes")
# plt.xlim([0, 400])

ax[0,1].hist(qual_dist, bins= n_bins)
ax[0,1].set_xlabel("quality of ref")
ax[0,1].set_ylabel("frequency")
ax[0,1].set_title("Quality Distribution")
# plt.xlim([0, 400])

ax[1,0].hist(allele_dist, bins= n_bins)
ax[1,0].set_xlabel("# of alleles")
ax[1,0].set_ylabel("frequency")
ax[1,0].set_title("Allele Frequency")
# plt.xlim([0, 400])

ax[1,1].bar(list(ann_list.keys()), list(ann_list.values()))
ax[1,1].set_xlabel("variant types")
plt.xticks(rotation = 90)
ax[1,1].set_ylabel("occurence in variants")
ax[1,1].set_title("The Number of Predicted Variants Occuring")
plt.tight_layout()
fig.savefig('multipanel_plot.png')
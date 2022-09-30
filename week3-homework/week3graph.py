#!/usr/bin/env python
import sys
import matplotlib.pyplot as plt



final = open("test.vcf", "r")

# #The read depth distribution of variant genotypes (histogram)
# read_depth = []
# n_bins = 500
#
# fig, ax = plt.subplots() # all will share the y axis
# for line in final:
#     if line[0] == "#":
#         continue
#     line2 = line.split("\t")
# # print(line2)
#     col_info = line2[7]
# # print(col_info)
#     genetype_info = col_info.split(";")
#     dp = genetype_info[7]
#     dp = dp.split(",")
#     dp = dp[0] # gives the DP=
#     act_dp = dp[3:] # give the number
#
#     read_depth.append(int(act_dp))
#
# ax.hist(read_depth, bins= n_bins)
# ax.set_xlabel("# of variant gentoypes")
# ax.set_ylabel("frequency of variant genotypes")
# ax.set_title("Distribution of Variant Genotypes")
# plt.xlim([0, 400])
# plt.savefig("wk3_a.png")
# plt.close()
# #
# # # The quality distribution of variant genotypes (histogram)
# qual_dist = []
# n_bins = 500
#
# fig, ax = plt.subplots()
# for line in final:
#     if line[0] == "#":
#         continue
#     line3 = line.split("\t")
# # print(line2)
#     col3_info = line3[7]
# # print(col_info)
#     qual_info = col3_info.split(";")
#     qr = qual_info[28]
#     qr = qr.split(",")
#     qr = qr[0] # gives the DP=
#     act_qr = qr[3:] # give the number
#     qual_dist.append(int(act_qr))
#
# ax.hist(qual_dist, bins= n_bins)
# ax.set_xlabel("quality of ref")
# ax.set_ylabel("frequency")
# ax.set_title("Quality Distribution")
# plt.xlim([0, 400])
# plt.savefig("wk3_b.png")
# plt.close()
#
# # The allele frequency spectrum of your identified variants (histogram)
# allele_dist = []
# n_bins = 500
#
# fig, ax = plt.subplots()
# for line in final:
#     if line[0] == "#":
#         continue
#     line4 = line.split("\t")
# # print(line2)
#     col4_info = line4[7]
# # print(col_info)
#     allele_info = col4_info.split(";")
#     af = allele_info[3]
#     af = af.split(",")
#     af = af[0] # gives the DP=
#     act_af = af[3:] # give the number
#     allele_dist.append(float(act_af))
#
# ax.hist(allele_dist, bins= n_bins)
# ax.set_xlabel("# of alleles")
# ax.set_ylabel("frequency")
# ax.set_title("Allele Frequency")
# # plt.xlim([0, 400])
# plt.savefig("wk3_c.png")
# plt.close()

# # A summary of the predicted effect(s) of each variant as determined by snpEff (barplot)
ann_list = []
n_bins = 500

fig, ax = plt.subplots()
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
    ann5 = ann4[0] # gives the DP=
    act_ann = ann5[4:5] # give the number
    ann_list.append(str(act_ann))

ax.bar(ann_list)
# ax.set_xlabel("")
# ax.set_ylabel("")
# ax.set_title("")
plt.savefig("wk3_d.png")
plt.show()
#
#



#!/usr/bin/env python
# from bring in the function
from bdg_loader import load_data
import matplotlib.pyplot as plt



 
D0_H3K27ac = load_data("D0_H3K27ac_scale_c.bdg")
D2_H3K27ac = load_data("D2_H3K27ac_scale_c.bdg")
R2_tc = load_data("R2_treat_scale_c.bdg")
R1_tc = load_data("R1_treat_scale_c.bdg")

#outputs x and y in dict called data

#step 5 graph
fig, ax = plt.subplots(ncols= 1, nrows=4)
ax[0].fill_between(D0_H3K27ac['X'], D0_H3K27ac["Y"])
ax[1].fill_between(D2_H3K27ac['X'], D2_H3K27ac["Y"])
ax[2].fill_between(R2_tc['X'], R2_tc["Y"])
ax[3].fill_between(R1_tc['X'], R1_tc["Y"])
plt.savefig("wk5_a.png")





#this code creates an array of 0s based upon the reads that overlap in the whole genome

#!/usr/bin/env python3
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt
from statsmodels.stats.multitest import multipletests

genome_reads_complete = np.zeros(1000000) # empty array of 1 million

positions = np.random.randint(999900, size = 50000)

for i in range(50000): # looking for 100bp
    positions = np.random.randint(0, high=999900)
    for g in range(positions, positions+100):
         genome_reads_complete[g] += 1




fig, ax = plt.subplots()
plt.hist(genome_reads_complete, label = "Distribution") #add labels
x = np.arange(0, 25, 1)
y = poisson.pmf(x, 5)*1000000 #gives distribution of the 1 million reads (tells how many reads possible )
ax.plot(x, y, label= "poisson") #add labels
ax.set_xlabel('covergae of reads')
ax.set_ylabel('frequencies')
ax.legend()
ax.set_title("5x coverage for 1Mbp of 100bp reads")
plt.show()
plt.savefig("wk1_5X.png")

# this reads the amount not covered
non_reads =[]
for i in genome_reads_complete:
    if i == 0:
        non_reads.append(1)

# how it matches the poisson distribution
matches = poisson.pmf(x, 15)*100000
print(matches)  #gives the amount of reads for a bin that are not covered, the possibilities of the coverage area

genome_reads_complete_2 = np.zeros(1000000)

for i in range(150000): # looking for 100bp
    positions_2 = np.random.randint(0, high=999900)
    for g in range(positions_2, positions_2+100):
         genome_reads_complete_2[g] += 1


#for 15X coverage
fig, ax = plt.subplots()
plt.hist(genome_reads_complete_2, label = "Distribution") #add labels
x = np.arange(0, 50, 1)
y = poisson.pmf(x, 15)*1000000 #gives distribution of the 1 million reads (tells how many reads possible )
ax.plot(x, y, label= "poisson") #add labels
ax.set_xlabel('number of reads')
ax.set_ylabel('coverage of reads')
ax.legend()
ax.set_title("15x coverage for 1Mbp of 100bp reads")
plt.show()
plt.savefig("wk1_b.png")







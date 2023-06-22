import numpy as np
import matplotlib.pyplot as plt

#simulation of the wrightfisher model
def wrightfisher(f, P):
    new_genf = []
    new_af = f
    while new_af != 0 and new_af != 1:
        allele_new = np.random.binomial(P, new_af) # reutrns the amount of people in next gen with allele
        new_af = allele_new/ P # returns the allelic freq of allele_new
        new_genf.append(new_af)
    return new_genf

#line plot code for simulation
f = 0.5
P = 100

def wfplot(f, P):
    y = wrightfisher(f,P) #allelic frequency
    x = np.arange(len(y)) #generation number

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)
    ax.set_xlabel("generation number")
    ax.set_ylabel("allele frequency")
    ax.set_ylim(0, 1)
    ax.set_title("Starting allele frequency " + str(f) + ", Population size " + str(P))
    plt.savefig("WrightFisher_sim2.png")


runs = np.arange(1000) #arange pulls a list for defined num
fix_t = []
for i in runs:
    fix_t.append(len(wrightfisher(0.5, 100)))


x = fix_t

fig, ax = plt.subplots()

ax.hist(x, bins=30, linewidth=0.5, edgecolor="white")
ax.set_xlabel("generation number")
ax.set_ylabel("# of generations for fixation")
ax.set_title("Generation Fixation")
plt.savefig("WF_GenerationFixation3.png")

#changing population size
pop_size = [100, 1000, 10000, 100000, 1000000, 100000000]
count_gen = []
for i in pop_size:
    count_gen.append(len(wrightfisher(0.5, i)))
 
y = count_gen
x = pop_size

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)
ax.set_xlabel("population size")
ax.set_ylabel("# of generations to fixation")
ax.set_xscale('log')
ax.set_title("Time for Fixation for Varying Population")
plt.savefig("WF_FixationVaryingPop4.png")

pop_size = [100, 1000, 10000, 100000, 1000000, 10000000]
count_gen = []
for i in pop_size:
    count_gen.append(len(wrightfisher(0.5, i)))

#changing allele frequency
af_size = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
count_gen1 = []
runs1 = np.arange(100) #arange pulls a list for defined num
final = []
for i in af_size:
    fix_af = []
    for j in runs1:
        fix_af.append(len(wrightfisher(i, 100)))
        
    final.append(fix_af)

D = final

# plot
fig, ax = plt.subplots()
ax.boxplot(D, labels = af_size)
ax.set_title('')
ax.set_xlabel('Allele frequency')
ax.set_ylabel('Time for fixation over generation')
plt.show()
plt.savefig("WF_FixationGeneration5.png")


    
    




#!/usr/bin/env python3

import numpy as np
import sys as sys
from fasta import readFASTA

input_sequences = readFASTA(open(sys.argv[1])) # this allows for inout arguments <CCTCF_38_M27_AA.faa> <scoring_matrix> <-2> <
scoring_matrix = (sys.argv[2])
penalty_gaps = float(sys.argv[3])
file_path = sys.argv[4]

 
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
# print(seq1_id, sequence1)
N_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
trace_m = np.zeros((len(sequence1)+1, len(sequence2)+1), dtype=str)
# print(N_matrix)
# print(len(sequence1))
# print(len(sequence2))
for i in range(len(sequence1)+1):
    N_matrix[i, 0] = i * penalty_gaps
    trace_m[i, 0] = "v"

for j in range(len(sequence2)+1):
    N_matrix[0,j] = j * penalty_gaps
    trace_m[0,j] = "h"

trace_m[0,0] = "e"
    
# print(scoring_matrix)
score_m = {}


f = open(scoring_matrix, "r")
line1 = f.readline()
for i, j in enumerate(line1.split()):
    score_m[j] = i
data = np.loadtxt(scoring_matrix, skiprows=1, usecols=range(1,len(score_m)+1))
 
f.close()



for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
 # if sequence1 and sequence2 match at positions i and j, respectively...
        d = N_matrix[i-1, j-1] + data[score_m[sequence1[i-1]], score_m[sequence2[j-1]]]
        # else: # if sequence1 and sequence2 don't match at those positions...
#             d = N_matrix[i-1, j-1] + mismatch_score
        h = N_matrix[i,j-1] + penalty_gaps
        v = N_matrix[i-1,j] + penalty_gaps

        N_matrix[i,j] = max(d,h,v)
        if d == N_matrix[i,j]:
            trace_m[i,j] = "d"
        elif h == N_matrix[i,j]:
            trace_m[i,j] = "h"
        else:
            trace_m[i,j] = 'v'


tot_seq1 = ""
tot_seq2 = ""

i = len(sequence1)
j = len(sequence2)

while trace_m[i][j] != 'e':
    if trace_m[i][j] == 'h': # if the index at this posiiton is h then go to the left and make a dash for the mismatch in x positioon
        tot_seq1 += '-'
        tot_seq2 += sequence2[j-1]
        j -=1
    elif trace_m[i][j] == "d": # if the index is at this position
        tot_seq1 += sequence1[i-1]
        tot_seq2 += sequence2[j-1]
        i -= 1
        j -= 1
    elif trace_m[i][j] == "v":
        tot_seq1 += sequence1[i-1]
        tot_seq2 += '-'
        i -= 1

rev_seq1 = tot_seq1[::-1]
rev_seq2 = tot_seq2[::-1]

actseq = open(file_path, 'w')
actseq.write(tot_seq1)
actseq.write(tot_seq2)
actseq.close()


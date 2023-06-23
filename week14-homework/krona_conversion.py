#!/usr/bin/env python

#USAGE: python scriptname.py KRAKEN_sample_input_file.kraken sample_name
#EXAMPLE: python make_krona_compatible.py KRAKEN/SRR492183.kraken SRR492183

import sys

f = open(sys.argv[1])
sample = sys.argv[2]
out = open(sample + "_krona.txt", "w")


for line in f:
    fields = line.strip('\r\n').split(';')
    out.write("\t".join(fields[1:]) + "\n")
    
    
#SRR492183.kraken	SRR492189.kraken	SRR492194.kraken
#SRR492186.kraken	SRR492190.kraken	SRR492197.kraken
#SRR492188.kraken	SRR492193.kraken	assembly.kraken
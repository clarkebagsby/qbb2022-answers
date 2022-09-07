#!/usr/bin/env python3
# chr21   5583465 5589528 ENST00000623887.1       0       +       5583465 5583
import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int] #this takes in 8 args instead of just 6
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if not (3 <= fieldN <= 9 or fieldN == 12):
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        
        if fieldN >= 9: #will look for columns greater than or equal to 9
            rgb = fields[8] #will put the 9th column into variable rgb
            rgb = rgb.split(',') #will seperate the string by commas 
            assert len(rgb) == 3        
        
        if fieldN >= 10: 
            blockStart = fields[9]
            #blockStart = blockStart.rsplit(',').split(',')
            print(blockStart)
               
        try:
            for j in range(min(len(field_types), len(fields))):
                if j < 9: 
                    fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
    
    fs.close()
    return bed
    
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)

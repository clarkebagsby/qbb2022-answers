#!/usr/bin/env python3

#This parser extends a BED file: ADD IN MORE ABOOUT WHAT THIS DOES
import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    
    field_types = [str, int, int, str, float, str, int, int] #this takes in 8 args instead of just 6 ; list oof what is expected
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        #print(fields)
        fieldN = len(fields)
        if not (3 <= fieldN <= 9 or fieldN == 12):
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue

        try:
            for j in range(min(len(field_types), len(fields))): #loops thru 0-5
                if j < 9:
                    fields[j] = field_types[j](fields[j]) # usiing field_types as a function to change it as data type
                    # 9,11
            
            if fieldN >= 9: #will look for columns greater than or equal to 9
                rgb = fields[8] #will put the 9th column into variable rgb
                rgb = rgb.split(',') #will seperate the string by commas
                assert len(rgb) == 3
            
            if fieldN >= 10:
                blockStart = fields[10]
                blockNumber = int(fields[9])
                fields[9] = blockNumber
                blockStart = blockStart.rstrip(',').split(',')
                assert len(blockStart) == blockNumber
            

            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)

    fs.close()
    return bed
    
if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = [] #will hold the entire file
    info_description = {} #info about headers and sections
    info_type = {} # for a certain field in info, going to tell us the type of info
    format_description = {} # stores genotype formats
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        } #key = datatyppe, value= is what is being converted
    malformed = 0 # startiing counter

    try:
        fs = open(fname) #tryiing to open file name 
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) #if the file is not found then will print error 

    for h, line in enumerate(fs): #goes through each line in the file h is line #
        if line.startswith("#"): #for the header, "if this is a header"
            try: #formats the header 
                if line.startswith("##FORMAT"): #see if its a format line
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header") #error mssg showed when headeer is incorrect
        else: #looking at variants, the body 
            try:# checking to see if variant sect is formatted correctly 
                fields = line.rstrip().split("\t") #making a list of column info and splitting by tabs
                fields[1] = int(fields[1]) #changing the position column(1) into int
                if fields[5] != ".": # looks at qual column 
                    fields[5] = float(fields[5]) # changes whatever is there into a float
                info = {} #new dictionary 
                for entry in fields[7].split(";"): #taking info str into a list, and lookiing at each str
                    temp = entry.split("=") #a list of before equals and after equals
                    if len(temp) == 1: #flag: no value associated, looks at each str to make sure that it is 0
                        info[temp[0]] = None #will say none if temp is longer than 1
                    else: #looks for those with equal 
                        name, value = temp # name before equals, value after equals, sets variable to both those values
                        Type = info_type[name] #looks through the info_type dict. to match datatype of name(previous )
                        info[name] = type_map[Type](value) #pulls funct type_map, to change data_type in info dict.  
                fields[7] = info #inserts dict. info for 
                if len(fields) > 8: #the file does not have genetype info, so looking at those files 
                    fields[8] = fields[8].split(":") #formatting for geneotype info, and replaces the 9th column, makes a list from those values
                    if len(fields[8]) > 1: # looking at indexes of all the genotypes of people in the file, checking for the len of genotype info to be greater than 1
                        for i in range(9, len(fields)): #starts at 1st genetype info( after 10th column)
                            fields[i] = fields[i].split(':')#turning geneotype field into a list and replaces fields[i] with the new list
                    else: 
                        fields[8] = fields[8][0] #only 1 thing, store that as a list
                vcf.append(fields) #sticking field list with formats into vcf
            except:
                malformed += 1 
   
    vcf[0][7] = info_description #replaces 
    if len(vcf[0]) > 8: #
        vcf[0][8] = format_description #puts in header info.
    if malformed > 0: #looks at if malformed has reached a value greater than 0, then prints statement and formats with malform
        print(f"There were {malformed} malformed entries", file=sys.stderr) #takes malformed variable and 
    return vcf

if __name__ == "__main__": 
    fname = sys.argv[1] #whatever you give as a filename 
    vcf = parse_vcf(fname) #running the file on the function created and storing output in vcf
    for i in range(10): #prints first ten lines (lines 0-9)
        print(vcf[i])

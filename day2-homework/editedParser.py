#data in random_snippet is not present in dbS
#goal: get variant ID from dbsnp and annotate in ran
# to compare db to ran, need pos, chrom, ref
# read two files using vcf_parser -->define output in two variables 
# run thru dbSNP, storing ID info for each variant -->store chrom, ID into key, value-variant ID
    #
    # make empty dict. variations = {}
    # for loop over vcf list (ignore first line)
    # for line in dbSNP_vcf: c
    #   chrom = line[0], pos = line[1], ref = line[3], id = line
    #   variations[]= ID # creates a dictionary of dbSNP with 
# run thru rand. -->pull out ID, look up ID based on chrom, pos, ref 
# 
import sys
import vcfParser 

random_snippet = vcfParser.parse_vcf("random_snippet.vcf")
dbSNP = vcfParser.parse_vcf("dbSNP_snippet.vcf")
dbSNP_dict = {}

for line in dbSNP:
    if line[0] == "CHROM":
        continue
    chrom = line[0]
    pos = line[1]
    Id = line[2]
    dbSNP_dict[(chrom, pos)] = Id

count = 0
for line in random_snippet:
    if line[0] == "CHROM": # skips the header
        continue
    rchrom = line[0]
    rpos = line[1]
    rId = line[2]
    
    if (rchrom, rpos) in dbSNP_dict:
        line[2] = dbSNP_dict[(rchrom, rpos)] # value of the key it matches
    else:
        count += 1
print(count)
        
        
   
        
    
    
    
    
        
        
    


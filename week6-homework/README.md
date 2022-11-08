# QBB-Week 6-Homework Codes + Answers 

# Part 1:code
curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/hicpro_analysis.tar.gz --output hicpro_analysis.tar.gz
tar -xzvf hicpro_analysis.tar.gz

curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/3dgenome_data.tar.gz --output 3dgenome_data.tar.gz
tar -xzvf 3dgenome_data.tar.gz

**instructions from assignment** : The hic_results has all of the data once reads have been assigned to restriction fragments.load_data.py is to read the matrix and bin files when you plot the heatmaps 
** Clarke**: focus on the ~/qbb2022-answers/week6-homework/analysis/hic_results \directory and subdirectories "pic"/ "matrix"
	# use as input for plotting
**Clarke **: focus on the ~/qbb2022-answers/week6-homework/3dgenome_data/matrix  and load_data.py
 

# Part 1: Answers
~ reading from the plotHiCContactrange graph, there are 92% of valid interactions. (got this from dCTCF file)
~ dangly ends that did not have a complementary pair to ligate to.

# Part 2:Code 

command for the sub-sampled 6400 res:
python load_data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed filtered1.png

load_data script contains the updated script for subsampled and the full data !
~ yes, the highlighted difference refers to shifting of the data from ddCTCF and dCTCF
~ were able to see the difference between interactions amoung different locuses 
~ the highlighted signal indicates the insulator interactions with enhancer regions, with a CTCF site you see less of the transcripts

command for insulation 4000 res:
python load_data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/3dgenome_data/matrix/dCTCF_full.40000.matrix 
/Users/cmdb/qbb2022-answers/week6-homework/3dgenome_data/matrix/40000_bins.bed /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed almost.png

forgot to do full data will add tomorrow!









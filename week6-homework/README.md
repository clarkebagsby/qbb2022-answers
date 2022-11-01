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
CLARKE: use the data in analysis/hic_results/matrix/dCTCF\ddCTCF 
~/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced --> input data in dCTCF_ontarget_6400_iced.matrix

python load_data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed filtered1.png

for insulation scores : in ~/qbb2022-answers/week6-homework/3dgenome_data/matrix/dCTCF_full.40000.matrix and ~/qbb2022-answers/week6-homework/3dgenome_data/matrix/40000_bins.bed


python load_data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix
 /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/3dgenome_data/matrix/dCTCF_full.40000.matrix  /Users/cmdb/qbb2022-answers/week6-homework/3dgenome_data/matrix/40000_bins.bed
/Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed filtered1.png

 
python load_data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/3dgenome_data/matrix/dCTCF_full.40000.matrix 
/Users/cmdb/qbb2022-answers/week6-homework/3dgenome_data/matrix/40000_bins.bed /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed 
almost.png










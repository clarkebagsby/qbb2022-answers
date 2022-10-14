
#QBB-Week 5-homework, codes

#Step 1 code
samtools view -q 10 *.bam
samtools view -q 10 D2_Sox2_R1.bam -b > D2_Sox2_R1_filtered.bam
#Step 2 code
#mm10 size 94987271 bp
macs2 callpeak -t D2_Sox2_R2_filtered.bam -c D2_Sox2_R2_input_filtered.bam -f BAM(optional) -g 94987271 -B -n R2
macs2 callpeak -t D2_Sox2_R1_filtered.bam -c D2_Sox2_R1_input_filtered.bam -f BAM -g 94987271 -B -n R1

#step 3 code
bedtools intersect -a R1_peaks.narrowPeak -b R2_peaks.narrowPeak -wa > R1R2intersected_peaks.bed

#Step 4 :40
bedtools intersect -a R1R2intersected_peaks.bam -b D2_Klf4_peaks.bed > Sox2_Klf4_intersected_peaks.bed

#Step 5 in assignments/lab/ChIP-seq/extra_datacp
python scale_bdg.py D0_H3K27ac_treat.bdg D0_H3K27ac_scale.bdg
python scale_bdg.py D2_H3K27ac_treat.bdg D2_H3K27ac_scale.bdg
python scale_bdg.py R1_treat_pileup.bdg R1_treat_scale.bdg
python scale_bdg.py R2_treat_pileup.bdg R2_treat_scale.bdg

awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D0_H3K27ac_scale.bdg > D0_H3K27ac_scale_c.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' D2_H3K27ac_scale.bdg > D2_H3K27ac_scale_c.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' R1_treat_scale.bdg > R1_treat_scale_c.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' R2_treat_scale.bdg > R2_treat_scale_c.bdg

#Part 2 
# 1 code
sort -k 5 -r -n R1R2intersected_peaks.bed > sorted_Sox2_ipeaks.bed
head -n 300 sorted_Sox2_ipeaks.bed > 300_Sox2_ipeaks.bed
awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' 300_Sox2_ipeaks.bed > new_Sox2_ipeaks.txt
samtools faidx -r new_Sox2_ipeaks.txt mm10.fa.fai > Sox2_KLF4_peaks.fasta
meme-chip Sox2_KLF4_peaks.fasta 
tomtom motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme combined.meme
tomtom combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
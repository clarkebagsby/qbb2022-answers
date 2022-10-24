# Week 3 Variant Calling -- Feedback

0 + 1 + 0.5 + 1 + 1 + 1 + 1 + 1 + 0.75 + 0 = 7.25 points out of 10 possible points

1. Index genome

  * what code did you use? --> +0

2. align reads

  * --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * what code did you use for sorting the bam files? --> +0.5

4. variant call with freebayes

  * perfect! --> +1

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * you can combine your for loops that extract the information to just loop through the file once
  * You want to use a [multipanel plot setup](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html#stacking-subplots-in-two-directions)
  * Would recommend extracting GQ not QR for the quality. You want the genotype quality and genotypes are sample specific
  * good script overall --> +1

9. 4 panel plot (0.25 points each panel)

  * the tick labels for the variant effect plot aren't readable and aren't aligned with the ticks. Try a `plt.tight_layout()` to see if the labels aren't cut off.
  * instead of 4 separate plots, you want a multipanel plot. You can make one of these in python by setting the number of rows and number of columns when you call `plt.subplots()` --> +0.75


10. 1000 line vcf

  * I don't see the vcf file. Did you do `git add --force <your.vcf>`?

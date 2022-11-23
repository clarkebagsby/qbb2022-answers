## Week 5 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0  = 9 points out of 10

1. Filter reads, Call peaks, and intersect peaks across Sox2 replicates (0.33 points each)

2. Find the number of total peaks and overlapping peaks for Klf4 and Sox2 (0.5 for commands, 0.5 for result)

3. scale bedgraph files (4 different datasets, 0.25 each)

4. crop bedgraph files (4 different datasets, 0.25 each)

5. python script for plotting

* good work using the returned dictionaries!

6. 4 panel plot of read pile ups

* Nice use of the tick marks and tick mark labels so that we can see the different scales. Most would prefer using the same scale/max value for all four subplots.
* Would be nice to add labels so we know which ChIP-seq reads are being plotted in each subpanel

7. motif finding sort intersected sox2 replicate narrow peak by 5th columm, keep first 300 lines, awk command for reformatting (0.33 each)

8. use samtools faidx to extract peak sequences and meme-chip to perform motif finding (0.5 each)

9. download and unpack motif database

* code for having done this? I see that you have based off of the tomtom command; just please record such things

10. match profiles from tomtom for klf4 and sox2 (0.5 for commands, 0.5 for result)

* grep command for this and then which tomtom matches are Klf4 or Sox2?

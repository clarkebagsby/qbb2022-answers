## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1 + 1 + 1 = 12 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

5. Script set up to shift the data by subtracting minimum value

* this means to subtract the minimum score value from all the scores. I see in your code where you try to shift by the start bin and so I think you just interpreted the instructions differently than intended. Still going to give you the points.

6. Script set up to convert sparse data into square matrix

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

* I see this one
* I'd recommend using a single vmax for the heatmaps so whichever has the higher max (heatmap_matrix or heatmap_matrix2)

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

* I didn't see this one submitted; I see this comment in your README: "load_data script contains the updated script for subsampled and the full data!", but the code you provide only runs `python load_data.py /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix /Users/cmdb/qbb2022-answers/week6-homework/analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed filtered1.png` for the sub-sampled 6400 res. Also see your comment "forgot to do full data will add tomorrow!", but sorry I don't see it.

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value
    * I see where you attempted this. You want to use [`np.amin(data_40kb_data['score'])`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html). Numpy `amin` works with vectors/arrays to find the minimum value there. Numpy `minimum` works with two vectors arrays to return the elementwise minimums, so comparing each index/location between the arrays and for a given location saying which value is lower. Numpy `argmin` returns the location in the array that is the minimum value in the array. Not sure why `min` didn't work without seeing the error message. It should be equivalent to `amin` based on documentation, but I use `amin`.
    * if you printed the variable `insulator_40kb_min2` and it was 42, then you used `argmin` perfectly

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)

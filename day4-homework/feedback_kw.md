# day 4 homework feedback

## Homework Exercise A & B

Great code! Very well done!

(I would recommend using the `vmin`, `vmax`, `xticklabels`, and `yticklabels` arguments/options within the `sns.heatmap()` function)

## Homework Exercise C

The heatmap that was turned in is blank and only represents the experiment without multiple hypothesis testing correction. You want two heatmaps -- one with multiple hypothesis testing correction and one without

## Homework Exercise D

You suggest that the axes are related in the following way:

>prob_heads= number of sperms
n_toss=  transmission rate

Looking at the axes in the plot, prob_heads are probabilities ranging from 0 to 1. Is that the case for number of sperm or transmission rate? I agree that your prob_heads is on the x-axis and the paper's x-axis is number of sperm. But theoretically, which ones are related in principle?

You are correct that for the coin toss the binomial test is used because there are two possible outcomes, heads or tails. Is this also the case for the transmission rate of an allele in a cohort of sperm? Do we expect only either allele 1 or allele 2?

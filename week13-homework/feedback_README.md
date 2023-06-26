Not necessarily "wrong", but I did want to note that your simulation as it currently exists is expecting the individuals to be haploid (or at least for the user to supply the population size as 2N). So when you run `wrightfisher(0.5, 100)`, that would either be simulating 100 haploid individuals, or 50 diploid individuals.

In your `WF_GenerationFixation3.png` figure, your x-axis label should be "# of generations to fixation" and your y-axis label should be "# of simulations", but the data itself is correct

For your `WF_FixationVaryingPop4.png` plot, I would recommend log-scaling both the x- AND y-axis, just so the relationship is a little clearer. You should see that there's a linear relationship between population size and time to fixation (which is why the larger population size simulations took so dang long

Your plot for part 5 didn't upload properly (or at least, I can't see it on my end for some reason), but I ran your code and the plot it produces looks great!

(10/10) Nice work!! 

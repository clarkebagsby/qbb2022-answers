## Week 11 Feedback


### Rubric

1. Filtering, using the Zheng 2017 method (0.5 point)
2. PCA plot before and after filtering (2 points)
	* Code (0.5 point each)
	* Plot (0.5 point each)
3. Apply leiden clustering (0.5)
4. tSNE and UMAP plots after clustering (2 points)
	* Code (0.5 point each)
	* Plot (0.5 point each)
5. Identify marker genes (1 point)
	* Code to identify groups with t-test and logistic regression (0.25 point)
	* Code to plot genes by cluster (0.25 point)
	* Genes by cluster plot (0.5 point)
6. Support plot for chosen 6 marker genes (2 points)
	* Code and plot (0.33 point for each marker gene)
7. tSNE or UMAP with labeled clusters (2 points)
	* Code to assign specific clusters a cell-type (1 point)
	* Code to create plot (0.5 point)
  * Plot (0.5 point)

### Grade

0.5 + 2 + 0.5 + 2 + 1 + 1 + 1.5  --> 8.5/10

I see the code for the later steps, but not the plots themselves. If you upload the support plots and then the labeled umap (labeling the clusters by proposed cell type), you should get full points.


### Regrade

Looks like you added both of the things Kate asked for! Nice work :D
I will note that it's not immediately clear to me how the code matches up with each of your output plots (not just the new plots, also the old plots). I suspect you had Python "show" the figures, and then save them, which is generally okay, but it makes it harder to know which bit of code made which plot. Better to use the `save` argument in `sc.pl.tsne()` or `sc.pl.umap()`, to tell it to save to a specific file

(10/10)

Dylan

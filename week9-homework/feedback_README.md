Great start! A few comments and things we need before this is complete:
1. For your qqplot, you need to manually set which distribution you want to compare against. The default distribution is a normal distribution, but do we expect pvals to be normally distributed? (-0.2 point)
2. You've gotten the transcripts from each model that are differentially expressed, but we need you to explicitly compare the overlap between the two sets of transcripts (-0.5 point)
3. We need your volcano plot for the model that includes sex. This should just be a scatter plot of -10log(pval) versus beta for each transcript. (-1 point)

(8.3/10)


REGRADE 07-24-2023 Dylan

Volcano plot and qqplot look great! For the qqplot, it looks like you're currently using the `line='q'` option, which I think tries to fit a line-of-best-fit to that curve, where instead we want just a 45 degree line (i.e y=x), because the null hypothesis is that the pval distribution matches the uniform distribution. So given that null, the 45 degree line represents the null hypothesis.

For the DE gene overlap, it still looks like you're giving me "DE with sex / DE without sex". It's possible that there are genes that are DE when you include sex that are not DE when you don't, but we're specifically interested in the intersection: the genes that are DE in both models. BUT this really isn't a big deal.

(10/10)

Awesome work! This all looks really good, and you just about nailed needleman-wunsch. A few very minor issues: first, you reversed your alignments after traceback (this is correct), but then you wrote the un-reversed alignments to the output file (no points deducted)

Also, when you're writing the alignments to the output, you actually have to specify that you want a newline character at the end of each line (otherwise both alignments are written to a single line, and that doesn't make sense) (no points deducted)

More importantly, something is going on with your DNA alignment, given your output, it looks like the two alignments aren't aligning at all, though they definitely should. Maybe you reversed the sign of the gap penalty? The way your code is written, you should be inputting a negative number as the gap penalty (-0.5)

You need to have your code print out statistics about the alignment (number of gaps in each sequence, and the alignment score). Make sure to upload this (for each alignment) in a README file (-1 point)

8.5/10

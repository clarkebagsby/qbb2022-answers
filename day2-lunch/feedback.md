# Feedback day2-lunch

This looks really good. There are a couple things missing in the parser, though. You don't split up blockSizes or check its length against blockNumber. You also don't do any type conversion to ints of itemRGB, blockStarts, or blockSizes. Finally, you are splitting fields 8 and 10, but those split values get lost because they are never saved anywhere. You need a statement saving the results back in fields[8] (or whichever). You also don't need the `if j < 9` statement as `len(field_types)` won't let j get that big, but it doesn't impact the function of the code any. All in all, this looks good. Also, I learned something new. I hadn't seen the use of ~ for indexing before! Keep up the good work!
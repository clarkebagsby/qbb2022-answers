#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys 
filename = sys.argv[1]
if len(sys.argv) > 2: 
  n_lines = int(sys.argv[2]) 
else: 
  n_lines = 10 

Store = []
for index in open(filename):
    Store.append(str(index))
print(Store)

count = 0
for line in Store:
    count = count + 1
    if count > n_lines and not line.startswith('#'):
        print(line.strip('\r\n'))
        
# This is SOOOOO close! You need to remove the first print statement, which I'm
# guessing was just to make sure you had saved the file into a list. The 
# condition in the if statement is not quite right. Right now instead of 
# printing the last "n_lines" lines, it will print the last len(Store) - n_lines
# lines. You could simply change it to "if count >= len(Store) - n_lines:" and 
# it would work. You also should get into the habit of commenting your code.
# It will make it easier to understand for you and others. Otherwise, it is clear
# that you understand what you are doing. Keep it up! - Mike
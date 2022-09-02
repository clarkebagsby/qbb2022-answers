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
        

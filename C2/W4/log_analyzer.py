import sys
import re

logfile = "all_logs.txt"
components = {}

with open(logfile) as f:
    for line in f:
        if "kernel" not in line:
            continue
        pattern = r"((^[ \w\d:]*PM|AM) (kernel: ([:\w]*)))"
        result = re.search(pattern, line)
        if result is not None:
            name = result[4]
            components[name] = components.get(name,0) + 1

            print("Time - {}\t  Component - {} \t".format(result[2],result[4]))

print(components)            


#to count the number of time error occured 
#for the comonent




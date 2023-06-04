#!/usr/bin/env python3

import os
import sys

#filename=sys.argv[1]
filename=input(str("filename : "))
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write('New file ceated\n')
else:
    print("Error,the file {} already exists!".format(filename))
    sys.exit(1)        

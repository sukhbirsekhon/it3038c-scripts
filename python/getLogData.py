import os 

filename = "test.txt"

with open(filename) as f:
    lines = set(f.read().splitlines())
    
    for line in lines: 
        if "sukhbir" in line:
            print(line)
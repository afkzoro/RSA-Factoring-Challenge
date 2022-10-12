#!/usr/bin/python3
import sys


try:
    file_name = sys.argv[2]
except Exception:
    raise TypeError("A file was not passed.")

count = 0

with open(file_name) as f:
    line = f.readlines()
    for i in line:
        count += 1
        lineNum = i.strip()
        if isinstance(lineNum, int) and lineNum > 1:
            try:
                for i in range(2, round(lineNum/2)):
                    result = lineNum % i
                    if result == 0:
                        print("{}={}*{}".format(lineNum, int(result), i))
                        break
            except Exception:
                pass

        else:
            raise TypeError("Not an integer")


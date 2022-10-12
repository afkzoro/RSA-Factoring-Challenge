#!/usr/bin/python3
"""Factorize as many numbers as possible into a product of two smaller numbers."""

import sys

try:
    file_name = sys.argv[2]
except Exception:
    raise TypeError("No file to read.")


count = 0

with open(file_name) as fp:
    Lines = fp.readlines()
    for line in Lines:
        count += 1
        lineValue = line.strip()
        if isinstance(lineValue, int) and lineValue > 1:
            try:
                for i in range(2,round(lineValue/2)):
                    result = lineValue % i
                    if result == 0:
                        print("{}={}*{}".format(lineValue,result,i))
                        break
            except Exception:
                pass
        else:
            raise TypeError("Data no valide at line {}. All line must conatin number gretter than 1 and no space arround the number.".format(count))

import sys
import math
from itertools import combinations, islice
from functools import reduce
from math import comb

"""
this code solve the "two piles difference" problem in codingame
https://www.codingame.com/ide/puzzle/the-two-piles-difference
"""

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
elements = []
n = int(input())
for i in input().split():
    value = int(i)
    elements.append(value)

lenn = comb(len(elements),len(elements)//2)

# Generate all possible 3-sized combinations of the numbers
combinations = combinations(elements, len(elements)//2)
half_combos = islice(combinations,0,lenn)


diff = 9999
for i in half_combos:
    temp = list(elements)
    sumA = 1
    for s in i:
        sumA *= s
    for j in i:
        temp.remove(j)
    sumB = sum(temp)**2
    ndiff = abs(sumA-sumB)
    if ndiff < diff:
        #print(ndiff)
        diff = ndiff
        if(diff == 0):
            break

print(diff)






# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


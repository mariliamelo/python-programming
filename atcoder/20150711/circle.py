# color circle areas
from math import pi

total = int(raw_input())

numbers = []

ratios = total
while ratios > 0:
    numbers.append(int(raw_input()))
    ratios -= 1

numbers.sort()

signal = 'tasu'
area = 0

while total > 0:
    ratio = float(numbers.pop())
    if signal == 'tasu':
        area += pi * ratio * ratio
        signal = 'minus'
    elif signal == 'minus':
        area -= pi * ratio * ratio
        signal = 'tasu'
    total -= 1
    
print area

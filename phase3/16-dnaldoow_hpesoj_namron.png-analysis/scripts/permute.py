#!/usr/bin/env python3

first = ['Z', 'Y']
second = ['G', 'Q']
third = ['J', 'G', 'Q', 'Y', 'W', 'T']

for p1 in first:
    for p2 in second:
        for p3 in third:
            print(p1 + p2 + p3)

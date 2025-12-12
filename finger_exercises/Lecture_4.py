#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:27:02 2025

@author: Itri26
"""

# Finger Exercises (Lecture 4)
# Assume you are given a positive integer variable named N.
# Write a piece of Python code that finds the cube root of N. 
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
# Hint: use a loop that increments a counter—you decide when the counter should stop.

N = 27
counter = 0
while counter**3 < N:
    counter += 1
if counter**3 == N:
    print(">",counter)
else:
    print("Error!")

# N = 28
# its_cube_root = False
# for i in range(N+1):
#     if i**3 == N:
#         print(">",i)
#         its_cube_root = True
# if not its_cube_root:
#     print("Error!")
        


# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 11: 2D Arrays
Objective
Today, we are building on our knowledge of arrays by adding another dimension.
Check out the Tutorial tab for learning materials and an instructional video.

Task
Given a 6 x 6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices
falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example
In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format
There are 6 lines of input,
where each line contains 6 space-separated integers that describe the 2D Array A.

Constraints
- -9 <= A[i][j] <= 9
- 0 <= i, j <= 5

Output Format
Print the maximum hourglass sum in A.

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19

Explanation
A contains the following hourglasses:
1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:
2 4 4
  2
1 2 4
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-24
Challenge End Date   =  2023-07-24
"""
#!/bin/python3

import math
import os
import random
import re
import sys


arr = []

def scan_array(arr):
    hourglass_sum_record = -9999999999
    for row in range(0, 4):
        for column in range(0, 4):
            hg_map_a = arr[row][column]
            hg_map_b = arr[row][column + 1]
            hg_map_c = arr[row][column + 2]
            hg_map_d = arr[row + 1][column + 1]
            hg_map_e = arr[row + 2][column]
            hg_map_f = arr[row + 2][column + 1]
            hg_map_g = arr[row + 2][column + 2]
            hourglass_sum = hg_map_a + hg_map_b + hg_map_c + hg_map_d + hg_map_e + hg_map_f + hg_map_g
            if hourglass_sum >= hourglass_sum_record:
                hourglass_sum_record = hourglass_sum
    return hourglass_sum_record

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
result = scan_array(arr)
print(result)
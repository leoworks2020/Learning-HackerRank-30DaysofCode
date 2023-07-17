# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 3: Intro to Conditional Statements
Objective
In this challenge, we learn about conditional statements.
Check out the Tutorial tab for learning materials and an instructional video

Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.

Input Format
A single line containing a positive integer, n.

Constraint
1 <= n <= 100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
3

Sample Output 0
Weird

Sample Input 1
24

Sample Output 1
Not Weird

Explanation
Sample Case 0:
n is odd and odd numbers are weird, so we print Weird.

Sample Case 1:
n > 20 and n is even, so it is not weird. Thus, we print Not Weird.

Challenge Start Date =  2023-07-17
Challenge End Date   =  2023-07-17
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def check_number(num):
    if num % 2 == 0:
        if num > 20:
            statement = "Not Weird"
        if num >= 6 and num <= 20:
            statement = "Weird"
        if num >= 2 and num <= 5:
            statement = "Not Weird"
    elif num % 2 != 0:
        statement = "Weird"
    return statement


N = int(input().strip())
result = check_number(N)
print(result)

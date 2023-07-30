# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 16: String to Integer
Objective
Today, we're getting started with Exceptions by learning how to parse an integer from a string and print a custom error message.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Read a string, S, and print its integer value;
if S cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs
built into your submission language.
If you attempt to use loops/conditional statements, you will get a 0 score.

Input Format
A single string, S.

Constraints
1 <= S <= 6, where |S| is the length of string S.

Output Format
Print the parsed integer value of S,
or Bad String if S cannot be converted to an integer.

Sample Input 0
3

Sample Output 0
3

Sample Input 1
za

Sample Output 1
Bad String

Explanation
Sample Case 0 contains an integer,
so it should not raise an exception when we attempt to convert it to an integer.
Thus, we print the 3.
Sample Case 1 does not contain any integers,
so an attempt to convert it to an integer will raise an exception.
Thus, our exception handler prints Bad String.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-29
Challenge End Date   =  2023-07-29
"""
#!/bin/python3

import math
import os
import random
import re
import sys

S = input()
try:
    S_int = int(S)
    print(S_int)
except:
	print("Bad String")

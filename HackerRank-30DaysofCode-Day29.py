# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 29: Bitwise AND
Objective
Welcome to the last day! Today, we're discussing bitwise operations.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given set S = {1,2,3,...,N}.
Find two integers, A and B (where A < B), from set S
such that the value of A & B is the maximum possible
and also less than a given integer, K.
In this case, & represents the bitwise AND operator.

Function Description
Complete the bitwiseAnd function in the editor below.

bitwiseAnd has the following parameter(s):
- int N: the maximum integer to consider
- int K: the limit of the result, inclusive

Returns
- int: the maximum value of A & B within the limit.

Input Format
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case
as 2 space-separated integers, N and K, respectively.

Constraints
- 1 <= T <= 10(**3)
- 2 <= N <= 10(**3)
- 2 <= K <= N

Sample Input
STDIN   Function
-----   --------
3       T = 3
5 2     N = 5, K = 2 S = {1,2,3,4,5}
8 5     N = 8, K = 5 S = {1,2,3,4,5,6,7,8}
2 2     N = 2, K = 2 S = {1,2]

Sample Output
1
4
0

Explanation
N = 5, K = 2 S = {1,2,3,4,5}
All possible values of A and B are:
01. A = 1, B = 2, A&B = 0
02. A = 1, B = 3, A&B = 1
03. A = 1, B = 4, A&B = 0
04. A = 1, B = 5, A&B = 1
05. A = 2, B = 3, A&B = 2
06. A = 2, B = 4, A&B = 0
07. A = 2, B = 5, A&B = 0
08. A = 3, B = 4, A&B = 0
09. A = 3, B = 5, A&B = 1
10. A = 4, B = 5, A&B = 4

The maximum possible value of A&B that is also < (K = 2) is 1, so we print 1 on a new line.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-08-11
Challenge End Date   =  2023-08-
v2 - Refactor to reduce execution time:

"""
#!/bin/python3

import math
import os
import random
import re
import sys

DBG = 0

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here

    #Create set with N elements
    numbers = []
    numbers = set()
    for i in range(1,N+1):
        numbers.add(i)

    #Loop to check bitwise
    first_number = list(numbers)[0]
    bitwise_AND_final_list = []
    while first_number < N:
        for second_number in range(first_number+1,len(numbers)+1):
            bitwise_AB_int = first_number & second_number
            if bitwise_AB_int == K-1:
                return bitwise_AB_int
            bitwise_AND_final_list.append(bitwise_AB_int)
        first_number += 1

    #Check max value for an integer below K
    result = find_max_less_than_given(bitwise_AND_final_list, K)
    return result


def find_max_less_than_given(numbers, given):
    find_max_less_than_given = max(filter(lambda x: x < given, numbers))
    return find_max_less_than_given


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        #fptr.write(str(res) + '\n')

    #fptr.close()
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
    if DBG == 1: print(f'numbers set = {numbers}')

    bitwise_max_value = 0
    bitwise_AB_values = []
    bitwise_AB_values_position = 0

    #Loop to check bitwise
    attempt = 0
    first_number = list(numbers)[0]
    while first_number < N and attempt < 999:
        for second_number in range(first_number+1,len(numbers)+1):
            attempt += 1
            bitwise_A_list = list(format(first_number, "08b"))
            bitwise_B_list = list(format(second_number, "08b"))

            #bitwise_A = [first_number, bin(first_number), str(bin(first_number))[-1:]]
            #bitwise_B = [second_number, bin(second_number), str(bin(second_number))[-1:]]
            #bitwise_A_list = list(bin(first_number))
            #bitwise_A_str = ''.join(map(str, bitwise_A_list))
            #bitwise_A_int = int(bitwise_A_str,2)
            #bitwise_A = format(bitwise_A_int, "08b")
            #bitwise_A_list = list(bitwise_A)


            #bitwise_B_list = list(bin(second_number))
            #bitwise_B_str = ''.join(map(str, bitwise_B_list))
            #bitwise_B_int = int(bitwise_B_str,2)
            #bitwise_B = format(bitwise_B_int, "08b")
            #bitwise_B_list = list(bitwise_B)

            bitwise_AB_list = []

            for i in range(0,8):
                bitwise_AB_item = int(bitwise_A_list[i]) * int(bitwise_B_list[i])
                bitwise_AB_list.append(bitwise_AB_item)
                #if int(bitwise_A_list[i]) == 1 and int(bitwise_B_list[i]) == 1:
                #    bitwise_AB_list.append(1)
                #else:
                #    bitwise_AB_list.append(0)
            bitwise_AB_str = ''.join(map(str, bitwise_AB_list))
            bitwise_AB_int = int(bitwise_AB_str,2)

            if bitwise_AB_int == K-1:
                return bitwise_AB_int

            #if DBG == 1: print(f'{attempt} - A = {bitwise_A_int}, B = {bitwise_B_int}, A&B = {bitwise_AB_int}')

            bitwise_AB_values.append(bitwise_AB_int)

        first_number += 1
    if DBG == 1: print(f'bitwise_AB_values: {bitwise_AB_values}')

    #Check which value in bitwise_AB_values is the maximum and still below K, then capture position
    bitwise_max_value = -1
    #for i in range(0,len(bitwise_AB_values)):
    #    if i == K or i+1 > len(bitwise_AB_values):
    #        break
    #    if bitwise_AB_values[i] >= bitwise_max_value:
    #        bitwise_max_value = bitwise_AB_values[i]
    #        bitwise_AB_values_position = i+1
    bitwise_final_list = bitwise_AB_values[:K]
    if K == 2 and N == 2:
        return bitwise_AB_values[0]
    else:
        for i in range(K-1,0,-1):
            if bitwise_final_list[i] == max(bitwise_final_list):
                bitwise_max_value = i
                #return bitwise_max_value
                return 999999
                # XXX - Deu bug com o input "184 105". E o bug tá acontecendo quando passa
                # XXX - Pelo return 999999 acima. Verificar passo a passo só com 184 105
                # XXX - para identificar o erro





DBG = 1
OUTPUT_PATH = "output/day29-output.txt"
INPUT_PATH = "input/"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #t = int(input().strip())
    with open("input/HackerRank-30DaysofCode-Day29-TestCase2.NumInputs.txt", "r") as f1:
        t = f1.readline()
        t = int(t)

    expected_list = []
    with open("input/HackerRank-30DaysofCode-Day29-TestCase2.Expected.txt", "r") as f3:
        while True:
            f3_line = f3.readline().replace("\n","")
            expected_list.append(f3_line)
            if not f3_line:
                break


    with open("input/HackerRank-30DaysofCode-Day29-TestCase2.Input.txt") as f2:
        f2_list = []
        while True:
            f2_line = f2.readline()
            f2_line = f2_line.replace("\n","")
            f2_line_split = f2_line.split(" ")
            f2_list.append(f2_line_split)
            if not f2_line:
                break
    t = len(f2_list)-1
    for t_itr in range(t):
        #first_multiple_input = input().rstrip().split()
        first_multiple_input = f2_list[t_itr]

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)
        if res != int(expected_list[t_itr]):
            print(f'Bug found!')
            print(f'res = {res}, expected = {expected_list[t_itr]}')
            input()
            #with open("input/HackerRank-30DaysofCode-Day29-TestCase2.Expected.txt", "w") as f3:
                #f3_write_line = f3.write(str(res))
        #if t_itr == lim:
        #    break
        #if DBG == 1: print(f'bitwise_operator_max = {res}')
        if DBG == 1: print(f'result = {res}')

        #fptr.write(str(res) + '\n')

    #fptr.close()
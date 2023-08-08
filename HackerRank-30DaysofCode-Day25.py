# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 25: Running Time and Complexity
Objective
Today we will learn about running time, also known as time complexity.
Check out the Tutorial tab for learning materials and an instructional video.

Task
A prime is a natural number greater than 1
that has no positive divisors other than 1 and itself.
Given a number, n, determine and print whether it is Prime or Not prime .

Note: If possible, try to come up with a O(**n) primality algorithm,
or see what sort of optimizations you come up with for an O(n) algorithm.
Be sure to check out the Editorial after submitting your code.

Input Format
The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints
- 1 <= T <= 30
- 1 <= n <= 2*10(**9)

Output Format
For each test case, print whether n is Prime or Not prime on a new line.

Sample Input
3
12
5
7

Sample Output
Not prime
Prime
Prime

Explanation
Test Case 0: n = 12.
12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 4, 6),
so we print Not prime on a new line.

Test Case 1: n = 5.
5 is only divisible 1 and itself, so we print Prime on a new line.

Test Case 2: n = 7.
7 is only divisible 1 and itself, so we print Prime on a new line.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-08-07
Challenge End Date   =  2023-08-
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_number(n):

    #Rule 1 - Number 1 is not Prime
    if n == 1:
        is_prime = False
        if debug ==1: print("Rule 1 match!")
        return is_prime

    #Rule 2 - Number 2 is the only even number which is Prime
    if n == 2:
        is_prime = True
        if debug ==1: print("Rule 2 match!")
        return is_prime

    #Rule 3 - Check if number has more than 2 factors
    prime_numbers_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if n in prime_numbers_list:
        is_prime = True
        if debug ==1: print("Rule 3 match!")
        return is_prime

    #Rule 5 - If number is even and not 2 then is not a Prime number
    if n % 2 == 0 and n != 2:
        is_prime=False
        if debug ==1: print("Rule 5 match!")
        return is_prime

    #Rule 4 - Checking number against a list of divisors numbers from 1 to 100
    is_prime = check_number_list(n)
    if is_prime == False:
        if debug ==1: print("Rule 4 match!")
        return is_prime

    #Rule 6 - Using formula 6n +- 1
    if int(n/6)*6+1 == n:
        is_prime = True
        if debug ==1: print("Rule 6 match!")
        return is_prime

    #Rule 7 - General Sqrt root of a number
    is_prime = check_sqrt_list(n)
    return is_prime


def check_sqrt_list(n):
    square_root = math.sqrt(n)
    square_root_list = []
    if debug ==1: print(square_root)
    for i in range(1,int(square_root)+1):
        if n % i == 0:
            square_root_list.append(i)
    square_root_list.append(n)
    if len(square_root_list) > 2:
        return False
    else:
        if debug ==1: print("Rule 8 match!")
        return True


def check_number_list(n):
    divisors_list = []
    for i in range(1,(10000000)+1):
        if n % i == 0:
            #print(n % i)
            divisors_list.append(i)
    if len(divisors_list) > 2:
        return False
    else:
        return True


import math
debug = 0

T=int(input())
for i in range(T):
    n = int(input())
    result = check_number(n)
    if result:
        print("Prime")
    else:
        print("Not prime")


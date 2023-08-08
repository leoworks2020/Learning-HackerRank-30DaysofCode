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

    #Rule 1 - Checking number against a list of divisors numbers from 1 to 100
    is_prime = check_number_list(n)
    if is_prime == True:
        print("Rule 1 match!")
        return is_prime

    #Rule 2 - If number is even and not 2 then is not a Prime number
    if n % 2 == 0 and n != 2:
        is_prime=False
        print("Rule 2 match!")
        return is_prime

    #Rule 3 - Number 3 is an exception for Rule 4
    if n ==3:
        is_prime=True
        print("Rule 3 match!")
        return is_prime

    #Rule 4 - Using formula 6n +- 1
    if int(n/6)*6+1 == n:
        print("Rule 4 match!")
        is_prime = True
        return is_prime


def check_number_list(n):
    division_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    divisors_list = []
    for i in range(len(division_list)):
        if n % division_list[i] == 0:
            divisors_list.append(i)
        print(f'divisors_list = {divisors_list}')
        if len(divisors_list) == 0:
            return True
        else:
            return False

T=int(input())
for i in range(T):
    n = int(input())
    result = check_number(n)
    if result:
        print("Prime")
    else:
        print("Not prime")



"""
https://www.cuemath.com/prime-numbers-formula/

BEST FORMULA:

Example 3: Check if 19 is a prime number or not using the prime numbers formula. 

Solution: 

The factors of 19 are 19 and 1.

Let us check if 19 can be represented using the prime numbers formula: 6n + 1

Divide 19 by 6. We get the remainder 1.

We can represent 19 as 6 × 3 + 1 

Therefore, 19 is a prime number. 
===================================================


Prime Numbers Formula Rules
Listed below are a few important aspects to be remembered while dealing with prime numbers and their formulas. 

Even numbers placed in the unit's place of any number cannot be a prime number
The number 2 is the only even prime number.
For large numbers, add all the digits together if the sum is divisible by 3 then it is not a prime number.
Except for numbers 2 and 3, all other numbers can be expressed using the prime numbers formula 6n ± 1, where, n = natural number


Formula 1: For any positive integer n,

(n+1) is prime if and only if n! ≡ n (mod n+1)

Formula 2: A prime number greater than 3 can be represented in the form: 6n ± 1

Prime number ≡ ± 1 (mod 6)

This method does not include the numbers that are multiples of prime numbers.

Formula 3: Prime numbers greater than 40 can be generated using:

n2 + n + 41


"""
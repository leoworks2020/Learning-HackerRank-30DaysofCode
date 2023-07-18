# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 5: Loops
Objective
In this challenge, we will use loops to do some math. Check out the Tutorial tab to learn more.

Task
Given an integer, n, print its first 10 multiples. Each multiple n x i
(where 1 <= i <= 10) should be printed on a new line in the form: n x i = result.

Example
n = 3
The printout should look like this:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

Input Format
A single integer, n.

Constraints
2 <= n <= 20

Output Format
Print 10 lines of output; each line i (where 1 <= i <= 10) contains the of n x i in the form:
n x i = result.

Sample Input
2

Sample Output
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-18
Challenge End Date   =  2023-07-18
"""
def do_multiply(number):
    # The loop will consider multiplications from 1 to 10
    for i in range (1,10+1):
        print(f'{number} x {i} = {number*i}')


try:
    input_number = int(input("Enter a number: "))
    do_multiply(input_number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
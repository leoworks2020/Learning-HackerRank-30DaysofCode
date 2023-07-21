# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 7: Arrays
Objective
Today, we will learn about the Array data structure.
Check out the Tutorial tab for learning materials and an instructional video.

Task
Given an array, A, of N integers, print A's elements in reverse order
as a single line of space-separated numbers.

Example
A = [1,2,3,4]
Print 4 3 2 1. Each integer is separated by one space.

Input Format
The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers that describe array A's elements.

Constraints
- 1 <= N <= 1000
- 1 <= A[i] <= 10000, where A[i] is the i(th) integer in the array.

Output Format
Print the elements of array A in reverse order as a single line of space-separated numbers.

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-20
Challenge End Date   =  2023-07-20
"""
n = int(input().strip())

numbers = list(map(int, input().rstrip().split()))
numbers.reverse()
reversed_numbers = ' '.join(map(str, numbers))
print(reversed_numbers)


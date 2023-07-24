# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 10: Binary Numbers
Objective
Today, we're working with binary numbers.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer
denoting the maximum number of consecutive 1's in n's binary representation.
When working with different bases, it is common to show the base as a subscript.

Example
n = 125

The binary representation of 125(base-10) is 1111101(base-2).
In base 10, there are 5 and 1 consecutive ones in two groups.
Print the maximum, 5.


Input Format
A single integer, n.

Constraints
1 <= n <= 10**6

Output Format
Print a single base-10 integer that denotes
the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1
5

Sample Output 1
1

Sample Input 2
13

Sample Output 2
2

Explanation
Sample Case 1:
The binary representation of 5(base-10) is 101(base-2),
so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13(base-10) is 1101(base-2),
so the maximum number of consecutive 1's is 2.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-23
Challenge End Date   =  2023-07-23
"""
def find_binary(number):
    binary_consecutive = 0
    binary_record = 0
    binary_number = str(bin(number))
    for n in range(len(binary_number)):
        if binary_number[n] in "abcdef":
            continue
        if int(binary_number[n]) == 1:
            binary_consecutive += 1
        else:
            binary_consecutive = 0
        if binary_consecutive >= binary_record:
            binary_record = binary_consecutive
    return binary_record


input_number = int(input())
result = find_binary(input_number)
print(result)
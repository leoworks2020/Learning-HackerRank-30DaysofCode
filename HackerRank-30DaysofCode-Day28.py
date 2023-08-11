# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 28: RegEx, Patterns, and Intro to Databases
Objective
Today, we're working with regular expressions.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Consider a database table, Emails, which has the attributes First Name and Email ID.
Given N rows of data simulating the Emails table,
print an alphabetically-ordered list of people whose email address ends in @gmail.com.

Input Format
The first line contains an integer, N, total number of rows in the table.
Each of the N subsequent lines contains 2 space-separated strings
denoting a person's first name and email ID, respectively.

Constraints
- 2 <= N <= 30
- Each of the first names consists of lower case letters [a-z] only.
- Each of the email IDs consists of lower case letters [a-z], @ and . only.
- The length of the first name is no longer than 20.
- The length of the email ID is no longer than 50.

Output Format
Print an alphabetically-ordered list of first names
for every user with a gmail account.
Each name must be printed on a new line.

Sample Input
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output
julia
julia
riya
samantha
tanya
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-08-10
Challenge End Date   =  2023-08-10
"""
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    email_list = list
    email_list = []
    print_list = []


    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        emailUser, emailDomain = emailID.split("@")

        email_record = [firstName,emailID,emailUser,emailDomain]
        email_list.append(email_record)


    i = 0
    while i < len(email_list):
        if email_list[i][3] == "gmail.com":
            print_list.append(email_list[i][0])
        i += 1

    print_list = sorted(print_list)

    for i in range(len(print_list)):
        print(print_list[i])




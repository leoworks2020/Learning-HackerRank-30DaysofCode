# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 26: Nested Logic
Objective
Today's challenge puts your understanding of nested conditional statements to the test.
You already have the knowledge to complete this challenge,
but check out the Tutorial tab for a video on testing.

Task
Your local library needs your help!
Given the expected and actual return dates for a library book,
create a program that calculates the fine (if any).
The fee structure is as follows:

1. If the book is returned on or before the expected return date,
no fine will be charged (i.e.: fine = 0).
2. If the book is returned after the expected return day
but still within the same calendar month and year as the expected return date,
fine = 15 Hackos x (the number of days late).
3. If the book is returned after the expected return month
but still within the same calendar year as the expected return date,
the fine = 500 Hackos x (thr number of months late).
4. If the book is returned after the calendar year in which it was expected,
there is a fixed fine of 10000 Hackos.

Example
d1, m1, y1 = 12312014 returned date
d2, m2, y2 = 112015 due date
The book is returned in the following year, so the fine is a fixed 10000.

Input Format
The first line contains 3 space-separated integers
denoting the respective day, month, and year on which the book was actually returned.
The second line contains 3 space-separated integers
denoting the respective day, month, and year
on which the book was expected to be returned (due date).

Constraints
- 1 <= D <= 31
- 1 <= M <= 12
- 1 <= Y <= 3000
- It is guaranteed that the dates will be valid Gregorian calendar dates.

Output Format
Print a single integer denoting the library fine for the book received as input.

Sample Input
STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)

Sample Output
45

Explanation
Given the following return dates:
Returned:   D1 = 9, M1 = 6, Y1 = 2015
Due:        D2 = 6, M2 = 6, Y2 = 2015

Because Y2 ≡ Y1, it is less than a year late.
Because M2 ≡ M1, it is less than a month late.
Because D2 < D1, it was returned late (but still within the same month and year).

Per the library's fee structure,
we know that our fine will be 15 Hackos x (# of days late).
We then print the result of 15 x (D1 - D2) = 15 x (9 -6) = 45 as our output.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-08-08
Challenge End Date   =  2023-08-
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
def calc_fine(return_date_list, due_date_list):
    calculated_fine = 0
    fine_count = 0
    return_date_day = int(return_date_list[0])
    return_date_month = int(return_date_list[1])
    return_date_year = int(return_date_list[2])
    return_date_serial = convert_date_to_serial(return_date_day, return_date_month, return_date_year)

    due_date_day = int(due_date_list[0])
    due_date_month = int(due_date_list[1])
    due_date_year = int(due_date_list[2])
    due_date_serial = convert_date_to_serial(due_date_day, due_date_month, due_date_year)

    #Condition 1 - No Fine (Book is returned before due date)
    if return_date_serial <= due_date_serial:
        return calculated_fine

    if return_date_year == due_date_year:
        if return_date_month == due_date_month:
            if return_date_day > due_date_day: # Condition 2 - 15 Hackos Fine - Day(s) late within same month and year
                fine_count = return_date_day - due_date_day
                return 15 * fine_count
        else: # Condition 3 - 500 Hackos Fine - Month(s) late within same year
            fine_count = return_date_month - due_date_month
            return 500 * fine_count
    else: # Condition 4 - 10000 Hackos Fixed Fine - Late over the calendar year
        return 10000

def convert_date_to_serial(day, month, year):
    # Specifying offset value i.e.,
    # the date value for the date of 1900-01-00
    offset = 693594

    input_date = date(year, month, day)
    n = input_date.toordinal()
    return (n - offset)



from datetime import date

DBG = 0

returned_date_list = input().split(" ")
due_date_list = input().split(" ")
fine = calc_fine(returned_date_list, due_date_list)
print(fine)
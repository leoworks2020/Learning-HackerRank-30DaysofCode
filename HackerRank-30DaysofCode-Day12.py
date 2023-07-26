# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 12: Inheritance
Objective
Today, we're delving into Inheritance.
Check out the attached tutorial for learning materials and an instructional video.

Task
You are given two classes, Person and Student,
where Person is the base class and Student is the derived class.
Completed code for Person and a declaration for Student are provided for you in the editor.
Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

- A Student class constructor, which has 4 parameters:
1. A string, fistName.
2. A string, lastName.
3. An integer, idNumber.
4. An integer array (or vector) of test scores, scores.
- A char calculate() method that calculates a Student object's average
and returns the grade character representative of their calculated average:

Grading Scale
Letter  Average (a)
O       90 <= a <= 100
E       80 <= a < 90
A       70 <= a < 80
P       55 <= a < 70
D       40 <= a < 55
T       a < 40

Input Format
The locked stub code in the editor reads the input
and calls the Student class constructor with the necessary arguments.
It also calls the calculate method which takes no arguments.

The first line contains firstName, lastName, and idNumber, separated by a space.
The second line contains the number of test scores.
The third line of space-separated integers describes scores.


Constraints
- 1 <= lenght of firstName, lenght of lastName <= 10
- lenght of idNumber = 7
- 0 <= score <= 100

Output Format
Output is handled by the locked stub code.
Your output will be correct if your Student class constructor
and calculate() method are properly implemented.

Sample Input
Heraldo Memelli 8135627
2
100 80

Sample Output
Name: Memelli, Heraldo
 ID: 8135627
 Grade: O

Explanation
This student had 2 scores to average: 100 and 80.
The student's average grade is (100+80)/2 = 90.
An average grade of 90 corresponds to the letter grade O,
so the calculate() method should return the character'O'.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-25
Challenge End Date   =  2023-07-25
"""
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)




# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here
    def calculate(self):
        average_score = int(sum(scores) / len(scores))
        if average_score < 0:
            average_score = 0
        if average_score > 100:
            average_score = 100
        if 90 <= average_score <= 100:
            student_final_grade = "O"
        elif 80 <= average_score < 90:
            student_final_grade = "E"
        elif 70 <= average_score < 80:
            student_final_grade = "A"
        elif 55 <= average_score < 70:
            student_final_grade = "P"
        elif 40 <= average_score < 55:
            student_final_grade = "D"
        elif 0 <= average_score < 40:
            student_final_grade = "T"
        return student_final_grade


# Receive 1st input which is firstName_lastName_idNumber in 1 line and break each element into a list (line)
line = input().split()
firstName = line[0]
firstName = firstName[:10]
lastName = line[1]
lastName = lastName[:10]
idNum = line[2]
idNum = idNum[:7]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores[0])
s.printPerson()
print("Grade:", s.calculate())
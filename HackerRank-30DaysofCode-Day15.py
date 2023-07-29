# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 15: Linked List
Objective
Today we will work with a Linked List.
Check out the Tutorial tab for learning materials and an instructional video.

A Node class is provided for you in the editor.
A Node object has an integer data field, data, and a Node instance pointer, next,
pointing to another node (i.e.: the next node in the list).

A Node insert function is also declared in your editor.
It has two parameters: a pointer, head, pointing to the first node of a linked list,
and an integer, data, that must be added to the end of the list as a new Node object.

Task
Complete the insert function in your editor so that it creates a new Node
(pass data as the Node constructor argument)
and inserts it at the tail of the linked list referenced by the head parameter.
Once the new node is added, return the reference to the head node.

Note: The head argument is null for an empty list.

Input Format
The first line contains T, the number of elements to insert.
Each of the next T lines contains an integer to insert at the end of the list.

Output Format
Return a reference to the head node of the linked list.

Sample Input
STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1

Sample Output
2 3 4 1

Explanation
T = 4, so your method will insert 4 nodes into an initially empty list.
First the code returns a new node that contains the data value 2 as the head of the list.
Then create and insert nodes 3, 4 and 1 at the tail of the list.

Initial:    head ---> null

                        Node n0
  T0:       head ---> [data = 2] [null]

                                             Node n1
  T1:       head ---> [data = 2] [n1] ---> [data = 3] [null]

                                                                   Node n2
  T2:       head ---> [data = 2] [n2] ---> [data = 3] [n2] ---> [data = 4] [null]

                                                                                       Node n3
  T3:       head ---> [data = 2] [n3] ---> [data = 3] [n2] ---> [data = 4] [n3] ---> [data = 1] [null]
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-07-28
Challenge End Date   =  2023-07-28
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        #Complete this method
        new_node = Node(data)  # Use Node inside the class
        current_item = head
        if current_item:
            # it already has a head, I have to go through the whole list and keep
            # checking to see if any of the nodes has a next that is empty (that is, None).
            while current_item.next:
                current_item = current_item.next
            current_item.next = new_node
        else:  # First element appended to Linked List
            head = new_node
        return head # Here the head will have data from new node appended as next to the previous one

mylist= Solution()
T=int(input())
head=None # head here is used to define the first item in the list. It starts as None since list is empty
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data) # Now head will be the result of creation of a new item
mylist.display(head);
# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 24: More Linked Lists
Objective
Check out the Tutorial tab for learning materials and an instructional video!

Task
A Node class is provided for you in the editor.
A Node object has an integer data field, data, and a Node instance pointer, next,
pointing to another node (i.e.: the next node in a list).

A removeDuplicates function is declared in your editor,
which takes a pointer to the head node of a linked list as a parameter.
Complete removeDuplicates so that it deletes any duplicate nodes
from the list and returns the head of the updated list.

Note: The head pointer may be null, indicating that the list is empty.
Be sure to reset your next pointer when performing deletions to avoid breaking the list.

Input Format
You do not need to read any input from stdin.
The following input is handled by the locked stub code
and passed to the removeDuplicates function:
The first line contains an integer, N, the number of nodes to be inserted.
The N subsequent lines each contain an integer
describing the data value of a node being inserted at the list's tail.

Constraints
- The data elements of the linked list argument will always be in non-decreasing order.

Output Format
Your removeDuplicates function should return the head of the updated linked list.
The locked stub code in your editor will print the returned list to stdout.

Sample Input
6
1
2
2
3
3
4

Sample Output
1 2 3 4

Explanation

N = 6, and our non-decreasing list is {1,2,2,3,3,4}.
The values 2 and 3 both occur twice in the list,
so we remove the two duplicate nodes.
We then return our updated (ascending) list, which is {1,2,3,4}.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-08-06
Challenge End Date   =  2023-08-
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        #Create a list from all nodes
        self.node_list_after = []
        self.node_list_data = []
        self.node_list_data_after = []

        ###self.node_list, self.node_list_data = self.scanNodes()

        # Iterate over the list removing duplicates
        ###self.node_list_after = self.node_list
        ###self.node_list_data_after = self.node_list_data
        ###self.node_list_range = len(self.node_list)


        node_data_list = []
        current = head
        while current:
            if current.data == current.next.data:
                current.next = current.next.next
                node_data_list.append(current.data)
            current = current.next
        if len(list(set(node_data_list))) != len(node_data_list):
            self.removeDuplicates(head)
        return head

"""
        i=0
        while self.node_list[i].next is not None:
            if self.node_list[i].data == self.node_list[i + 1].data:
                self.node_list[i].next = self.node_list[i + 1].next
                self.node_list_after.pop(i)
                self.node_list_data_after.pop(i)
                i = 0
            else:
                i += 1

            #if self.node_list[i].data == self.node_list[i + 1].data and self.node_list[i].next is not None:
            #    self.node_list[i].next = self.node_list[i + 1].next
            #    self.node_list_after.pop(i)
            #    self.node_list_data_after.pop(i)
            #    i = 0
            #if self.node_list[0].data == self.node_list[1].data and len(self.node_list) == 2:
            #    self.node_list[0].next = None
            #    return self.node_list[0]
        return self.node_list[0]

    def scanNodes(self):
        self.current_node = None
        self.next_node = None
        self.node_list = []
        self.node_list_data = []

        # Get total number of nodes in the linked list to create a for based on list length
        self.current_node = head
        while True:
            if self.current_node not in self.node_list:
                self.node_list.append(self.current_node)
                self.node_list_data.append(self.current_node.data)
                if self.current_node.next == None:
                    # Leave the while after capturing the last node in the list (the one which has no next)
                    break
                else:
                    self.current_node = self.current_node.next
        return self.node_list, self.node_list_data
"""

mylist = Solution()

test_case = [20,3,9,9,11,11,11,11,89,89,100,100,101,102,103,108,200,250,250,250,250]
#T = int(input())
T = test_case
head = None
for i in range(len(T)):
    data = int(test_case[i])
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head);
# Hacker Rank 30 Days of Code Challenges
#
"""
Challenge Day 22: Binary Search Trees
Today, we're working with Binary Search Trees (BSTs).
Check out the Tutorial tab for learning materials and an instructional video!

Task
The height of a binary search tree is the number of edges
between the tree's root and its furthest leaf.
You are given a pointer, root, pointing to the root of a binary search tree.
Complete the getHeight function provided in your editor
so that it returns the height of the binary search tree.

Input Format
The locked stub code in your editor reads the following inputs
and assembles them into a binary search tree:
The first line contains an integer, n, denoting the number of nodes in the tree.
Each of the n subsequent lines contains an integer, data,
denoting the value of an element that must be added to the BST.

Output Format
The locked stub code in your editor will print the integer
returned by your getHeight function denoting the height of the BST.

Sample Input
7
3
5
2
1
4
6
7

Sample Output
3

Explanation

The input forms the following BST:

Binary Search Tree
       3
     /  \
   2     5
 1      / \
       4   6
            \
             7

The longest root-to-leaf path is shown below:

Longest Root-to-Leaf Path
       3
        \
         5
          \
           6
            \
             7
 There are 4 nodes in this path that are connected by 3 edges,
 meaning our BST's height = 3. Thus, we print 3 as our answer.
----------------------------------------------------------------------------------------------------------
Challenge Start Date =  2023-08-04
Challenge End Date   =  2023-08-
"""
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        self.id = []
        self.node_list = []
        self.first_node = 0
        self.previous_node = 0
        self.height = 0
        self.max_height = 0
        self.id.append(root.data)
        self.node_list.append(root)
        self.previous_node = root
        self.iteration = 1

        if root.left == None and root.right == None:
            max_current = self.height
        else:
            while True:
                if root.left not in self.node_list and root.left is not None:
                    self.height += 1
                    self.node_list.append(root.left)
                    self.previous_node = root
                    root = root.left
                    self.iteration += 1
                elif root.right not in self.node_list and root.right is not None:
                    self.height += 1
                    self.node_list.append(root.right)
                    self.previous_node = root
                    root = root.right
                    self.iteration += 1
                else:
                    if self.iteration - 1 < 0:
                        print("FIM")
                        return self.max_height
                    root = self.previous_node
                    self.iteration -= 1
                #elif root.left in self.node_list and root.right not in self.node_list:
                #    root = root.right
                #    self.node_list.append(root.right)


                if root.left == None and root.right == None:
                    #max_height = self.height
                    #print("Found the bottom")
                    if self.max_height < self.height:
                        self.max_height = self.height
                    root = self.previous_node
                    self.iteration -= 1
                    self.height = 0
                    #break

            if root.left != None:
                self.id.append
            #root = root.left
        #Write your code here
#        height_left = 0
#        height_right = 0
        max_current = 0
        max_found = 0
        max_height_left = 0
        max_height_right = 0

        #Checking Left Side
        left_items = []
        while True:
            if root.left == None:
                max_current = len(left_items)
                break
            else:
                left_items.append(root.data)
                root = root.left

        # Checking Right Side
        left_items = []
        while True:
            if root.left == None:
                max_current = len(left_items)
                break
            else:
                left_items.append(root.data)
                root = root.left

        return max_current
 #           height_left.append("a")
 #           root = root.left
 #           self.getHeight(root)



T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
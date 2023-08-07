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
Challenge End Date   =  2023-08-06
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
        self.node_root = root
        self.node_list = []
        self.level = 0
        self.level_max = 0

        while True:
            if root.left is not None and root.left not in self.node_list:
                root = root.left
                self.level += 1
                if self.level_max < self.level:
                    self.level_max = self.level
            elif root.right is not None and root.right not in self.node_list:
                root = root.right
                self.level += 1
                if self.level_max < self.level:
                    self.level_max = self.level
            else:
                self.node_list.append(root)
                if root == self.node_root:
                    break
                root = self.node_root
                self.level = 0
        return self.level_max


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
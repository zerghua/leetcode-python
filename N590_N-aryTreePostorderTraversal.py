#
# Create by Hua on 5/18/22
#


"""
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)



Example 1:


Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]


Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.


Follow up: Recursive solution is trivial, could you do it iteratively?


"""
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        05/18/2022 14:23	Accepted	72 ms	16.4 MB	python
        easy 5 min.
        """
        def dfs(node, lt):
            if not node: return
            for child in node.children:
                dfs(child, lt)
            lt.append(node.val)

        ret = list()
        dfs(root, ret)
        return ret
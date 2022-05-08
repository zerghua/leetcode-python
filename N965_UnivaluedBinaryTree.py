#
# Create by Hua on 5/8/22.
#

"""
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.



Example 1:

Input: root = [1,1,1,1,1,null,1]
Output: true

Example 2:

Input: root = [2,2,2,5,2]
Output: false



Constraints:

    The number of nodes in the tree is in the range [1, 100].
    0 <= Node.val < 100


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        thought: tree traversal, check each value
        05/08/2022 10:26	Accepted	29 ms	13.3 MB	python
        easy 5-10 min.
        """

        def dfs(node, v):
            if not node: return True
            if node.val != v:
                return False

            return dfs(node.left, v) and dfs(node.right, v)

        return dfs(root, root.val)
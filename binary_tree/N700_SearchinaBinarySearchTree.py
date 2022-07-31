#
# Create by Hua on 5/18/22
#


"""
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.



Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        thought: in-order traversal
        05/18/2022 10:37	Accepted	115 ms	17.4 MB	python
        easy 5-10 min.
        """
        def dfs(node, val):
            if not node: return None
            if node.val == val:
                return node
            elif val < node.val:
                return dfs(node.left, val)
            else:
                return dfs(node.right, val)

        return dfs(root, val)
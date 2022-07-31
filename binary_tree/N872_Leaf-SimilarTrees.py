#
# Create by Hua on 5/12/22
#


"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Example 1:


Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:


Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false


Constraints:

The number of nodes in each tree will be in the range [1, 200].
Both of the given trees will have values in the range [0, 200].

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool

        thought: need a function to get the leaf value for each tree.
        tree traversal
        05/12/2022 15:30	Accepted	27 ms	13.5 MB	python
        easy 5 min.
        """
        def get_leaf(node, ret):
            if not node: return
            if not node.left and not node.right: ret.append(node.val)  # leaf node
            get_leaf(node.left, ret)
            get_leaf(node.right, ret)

        a, b = list(), list()
        get_leaf(root1, a)
        get_leaf(root2, b)
        return a == b
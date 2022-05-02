#
# Create by Hua on 5/2/22.
#

"""
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

    For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.



Example 1:

Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Example 2:

Input: root = [0]
Output: 0



Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    Node.val is 0 or 1.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int

        thought: tree traversal

            root
        left                right
        empty, non-empty

        05/02/2022 11:06	Accepted	35 ms	13.9 MB	python
        easy - medium 5-10 min.
        """
        def dfs(r, s):
            # root can't be null here
            cur = s + str(r.val)
            if r.left is None and r.right is None:  # leaf node
                return int(cur, 2)  # convert binary to int

            ret = 0
            if r.left:
                ret += dfs(r.left, cur)

            if r.right:
                ret += dfs(r.right, cur)

            return ret

        return dfs(root, "")

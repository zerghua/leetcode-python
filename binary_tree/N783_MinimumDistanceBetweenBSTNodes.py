#
# Create by Hua on 5/16/22
#


"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105


Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ret = 10**6
    pre = -1

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int

        thought: in-order traversal to compare adjacent nodes value
        [27,null,34,null,58,50,null,44]

            27
                34
                   58
                 50
              44

        o(1) space. o(n) space is much easier, convert bst to list using in-order

        pre has to be global, if passed it down, when recursion it might not get updated.
        05/16/2022 11:02	Accepted	10 ms	13.4 MB	python
        easy - medium 20-30 min. stuck on debugging the difference between pre to be global vs passed it down as
        argument.
        """
        def dfs(node):
            if not node: return
            dfs(node.left)
            if self.pre != -1: self.ret = min(self.ret, node.val - self.pre)
            self.pre = node.val
            dfs(node.right)

        dfs(root)
        return self.ret


class Solution2(object):
    ret = 10**6

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int

        thought: in-order traversal to compare adjacent nodes value
        [27,null,34,null,58,50,null,44]

            27
                34
                   58
                 50
              44

        o(1) space. o(n) space is much easier, convert bst to list using in-order

        05/16/2022 11:10	Accepted	36 ms	13.7 MB	python
        passed pre as argument using a mutable object

        # not using global variables
        class Solution(object):
            def minDiffInBST(self, root):
                mincount = [float('inf')]
                prev = [-float('inf')]
                self.getMin(root, mincount, prev)
                return mincount[0]

            def getMin(self, root, mincount, prev=None):
                if not root: return
                self.getMin(root.left, mincount, prev)
                mincount[0] = min(mincount[0], root.val-prev[0])
                prev[0] = root.val
                self.getMin(root.right, mincount, prev)
        """
        def dfs(node, pre):
            if not node: return
            dfs(node.left, pre)
            if pre[0] != -1: self.ret = min(self.ret, node.val - pre[0])
            pre[0] = node.val
            dfs(node.right, pre)

        dfs(root, [-1])
        return self.ret



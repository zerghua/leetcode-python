#
# Create by Hua on 5/10/22.
#

"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].



Example 1:

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.



Constraints:

    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int

        thought: tree traversal
        05/10/2022 10:01	Accepted	331 ms	29.7 MB	python
        easy 5-10 min.
        """

        if not root: return 0
        v = 0
        if low <= root.val <= high:
            v = root.val

        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + v

class Solution2(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int

        thought: tree traversal
        05/10/2022 10:07	Accepted	247 ms	29.7 MB	python
        easy 5-10 min.
        """

        if not root: return 0
        if root.val < low: return self.rangeSumBST(root.right, low, high)
        elif root.val > high: self.rangeSumBST(root.left, low, high)
        else: return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val


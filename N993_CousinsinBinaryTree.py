#
# Create by Hua on 5/7/22.
#

"""
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.



Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false



Constraints:

    The number of nodes in the tree is in the range [2, 100].
    1 <= Node.val <= 100
    Each node has a unique value.
    x != y
    x and y are exist in the tree.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        thought: BFS, in the same depth should find both x and y,
        and their parent is not the same
        05/07/2022 10:33	Accepted	25 ms	13.6 MB	python
        easy - medium: 20-30 min. more time spent on refreshing BFS.


        https://leetcode.com/problems/cousins-in-binary-tree/discuss/246883/Python-straightforward-and-clean-DFS
        dfs
        class Solution:
        def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
            def dfs(node, parent, depth, mod):
                if node:
                    if node.val == mod:
                        return depth, parent
                    return dfs(node.left, node, depth + 1, mod) or dfs(node.right, node, depth + 1, mod)
            dx, px, dy, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
            return dx == dy and px != py


        """

        if root.val in [x,y]:  # corner case root is x or y
            return False

        s = list()
        s.append(root)
        parent = list()
        while s:
            tmp = list()
            for node in s:  # list all nodes in one depth
                if node.left:
                    if node.left.val in [x,y]:
                        parent.append(node.val)
                    tmp.append(node.left)
                if node.right:
                    if node.right.val in [x,y]:
                        parent.append(node.val)
                    tmp.append(node.right)
            s = tmp
            if len(parent) == 1:
                return False
            if len(parent) == 2:
                if parent[0] != parent[1]:
                    return True
                return False




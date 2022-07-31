#
# Create by Hua on 5/12/22
#


"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        thought:
        https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
        didn't solve it the first time to use in-place adjustment.
        can do with extra space to do in-order traversal and build a new tree.
        in order traversal
        dfs(left) + root + dfs(right)

        05/12/2022 10:27	Accepted	28 ms	13.6 MB	python
        easy - medium 20-30min.
        """

        def inorder(node, nextnode):
            if not node: return nextnode
            newRoot = inorder(node.left, node)
            node.left = None
            node.right = inorder(node.right, nextnode)
            return newRoot

        return inorder(root, None)

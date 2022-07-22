#
# Create by Hua on 7/22/22
#

"""
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.



Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.


Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]

        thought: for each description, create a node, store each node in a dict, link each node to its children
        to find the root, also store a set of children, use all_node - children set to get root node.

        07/22/2022 09:33	Accepted	4885 ms	30 MB	python

        30-40min.
        medium. build trees using hashmap.

        https://leetcode.com/problems/create-binary-tree-from-descriptions/discuss/1823804/Python-Solution
        simpler code:
            def createBinaryTree(self, descriptions):
                children = set()
                m = {}
                for p,c,l in descriptions:
                    np = m.setdefault(p, TreeNode(p))
                    nc = m.setdefault(c, TreeNode(c))
                    if l:
                        np.left = nc
                    else:
                        np.right = nc
                    children.add(c)
                root = (set(m) - set(children)).pop()
                return m[root]
        """

        nodes = dict()   # node val is key, TreeNode is the val
        children = set()
        # build tree
        for node_val, child, is_left in descriptions:
            child_node = nodes[child] if child in nodes else TreeNode(child)
            if node_val in nodes:
                node = nodes[node_val]
                if is_left:
                    node.left = child_node
                else:
                    node.right = child_node
            else:
                node = TreeNode(node_val, child_node, None) if is_left else TreeNode(node_val, None, child_node)
            nodes[node_val] = node     # push into dict
            nodes[child] = child_node  # push into dict
            children.add(child)

        # find root
        root_val = list(set(nodes.keys()) - children)[0]
        return nodes[root_val]




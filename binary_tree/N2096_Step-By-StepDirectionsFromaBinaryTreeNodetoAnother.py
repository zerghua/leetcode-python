#
# Create by Hua on 7/31/22
#

"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.



Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str

        thought: need to find the LCA(Lowest common ancestor) of the start and dest node.
        then get the string from LCA to S, and LCA to d, replace LCA to S string as U string
        from root to find start and dest in 2 dfs, and remove the common part of both strings,
        change each char of first string to U and build the final answer.

        513(LL)
        526(RL)
        -> 31526 (UURL)

        526(RL) (5->6)
        524(RR) (5->4)
        - > 624 (UR)

        (2->2) ""
        (2->1) "L"
        -> L

        (2->1) "L"
        (2->2) ""
        ->  "U"

        07/31/2022 17:50	Accepted	880 ms	154.7 MB	python
        medium - hard
        1h
        binary tree find path.
        """
        def dfs(node, last, target):  # return true or false, find the path to target val
            if not node: return False
            if node.val == target:
                return True

            if node.left:
                last.append("L")
                if dfs(node.left, last, target):
                    return True
                last.pop(-1)  # backtracking

            if node.right:
                last.append("R")
                if dfs(node.right, last, target):
                    return True
                last.pop(-1)  # backtracking
            return False

        a,b = [],[]
        dfs(root, a, startValue)
        dfs(root, b, destValue)

        i = 0
        while i<(min(len(a), len(b))):
            if a[i] != b[i]:
                break
            i+=1
        a = a[i:]
        b = b[i:]
        return "U"*len(a) + "".join(b)


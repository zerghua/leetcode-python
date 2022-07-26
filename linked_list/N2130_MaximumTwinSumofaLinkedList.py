#
# Create by Hua on 7/26/22
#

"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.



Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.


Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int

        thought: need to reverse the second half of list.
        1->   2  -> 3
    pre,cur,next
        pre,cur,next
            pre,cur,next
                pre,cur

        07/26/2022 15:40	Accepted	1241 ms	72.2 MB	python
        medium - easy
        20-30min.
        linked list reverse
        """

        slow,fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next
        # now slow point the half of the list, let's reverse the second half, need 3 pointers
        pre, cur, next = None, slow, slow
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # now pre points to the last node
        ret = 0
        while pre:
            ret = max(ret, pre.val + head.val)
            pre = pre.next
            head = head.next

        return ret





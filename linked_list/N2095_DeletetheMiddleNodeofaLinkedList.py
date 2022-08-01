#
# Create by Hua on 8/1/22
#

"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.


Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        thought: 2 pointers.
        1, 2, 3, 4, 5
          p1, p2
              p1,  p2
        ending criteria is when p2 is None or p2.next is None, then p1 points to the middle.
        then another loop p0, if po.next is p1, then stop.
        corner case, only 1 node. if p1 == head, return None.

        08/01/2022 17:00	Accepted	3817 ms	97.6 MB	python
        medium - easy
        10-20 min.
        linked list, 2 pointers
        """

        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        if p1 == head: # corner case, only 1 node
            return None

        p0 = head
        while p0.next != p1:
            p0 = p0.next

        p0.next = p1.next
        return head



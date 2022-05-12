#
# Create by Hua on 5/12/22
#


"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        thought: if no-extra space, use 2 pointers. one pointer goes 1 step, another goes 2 steps each time
        1,2,3,4,5
        1,1 2,3 3,5->null

        1,2,3,4,5,6
        1,1 2,3 3,5 4,null

        if 2_pointer == None or 2_pointer.next == None, return 1_pointer

        05/12/2022 15:23	Accepted	14 ms	13.5 MB	python
        easy 5 min. 2 pointers.
        """

        a = head
        b = head
        while b and b.next:
            a = a.next
            b = b.next.next
        return a


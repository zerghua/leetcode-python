#
# Create by Hua on 4/16/22.
#

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.



Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [0]
Output: 0



Constraints:

    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int

        thought: convert linked list to list
        04/16/2022 15:33	Accepted	16 ms	13.5 MB	python
        easy 5 min.

        """
        a = list()
        while head:
            a.append(head.val)
            head = head.next

        ret = 0
        i = 0
        for n in a[::-1]:
            if n == 1:
                ret += 2 ** i
            i += 1
        return ret
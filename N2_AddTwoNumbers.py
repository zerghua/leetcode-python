# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

from N0_DataStructures import ListNode


# 164 ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 is not None and l2 is not None:
            total = l1.val + l2.val + carry
            carry = total/10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            total = l1.val + carry
            carry = total / 10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
            l1 = l1.next

        while l2 is not None:
            total = l2.val + carry
            carry = total / 10
            total %= 10
            cur.next = ListNode(total)
            cur = cur.next
            l2 = l2.next

        if carry == 1:
            cur.next = ListNode(1)

        return dummy.next

#
#  Create by Hua on 8/31/2016
#


"""
 Given a linked list, swap every two adjacent nodes and return its head.

 For example,
 Given 1->2->3->4, you should return the list as 2->1->4->3.

 Your algorithm should use only constant space.
 You may not modify the values in the list, only nodes itself can be changed.


    //  pre -->  cur --> next  --> next.next
    //  1.  pre/cur --> next --> next.next
    //  2.  pre --> next    cur --> next.next
    //  3.  pre --> next --> cur --> next.next

"""

# 36 ms  55 / 55 test cases passed.
# key is to use dummy node and operate on THREE links.
from N0_DataStructures import ListNode
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre =dummy
        dummy.next= head
        cur = head
        while cur is not None and cur.next is not None:
            next_node = cur.next
            pre.next = next_node
            cur.next = next_node.next
            next_node.next = cur
            pre = cur
            cur = cur.next
        return dummy.next
#
# Create by Hua on 8/4/22
#

"""
You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.



Example 1:


Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
Example 2:


Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.
Example 3:


Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 105

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]

        thought:
        A -> (B->.. ->C) -> D,
        A -> C -> B -> D
        each group size: 1, 2, 3, 4 ... n
        reverse the even count group
             b ->  c
         pre p    post  tail
             pre   p   post

         # handle first
         p.next = tail
         pre = p
         p = post
         post = post.next

         # handle middle
         while post != tail:
             p.next = pre
             pre = p
             p = post
             post= post.next

        # handle last
        start.next = p

        but a corner case is that the last group can be less than n, the last group can or can't be even.

        https://leetcode.com/problems/reverse-nodes-in-even-length-groups/discuss/1577032/Python-Reverse-Linked-List-O(1)-Space
        def reverseEvenLengthGroups(head):
            prev = head
            d = 2 # the head doesn't need to be reversed anytime so starts with length 2
            while prev.next:
                node, n = prev, 0
                for _ in range(d):
                    if not node.next:
                        break
                    n += 1
                    node = node.next
                if n & 1:  # odd length
                    prev = node
                else:      # even length
                    node, rev = prev.next, None
                    for _ in range(n):
                        node.next, node, rev = rev, node.next, node  # at the end of this line, rev is the pre of node
                    prev.next.next, prev.next, prev = node, rev, prev.next
                d += 1
            return head

            # a ,   b ,         c ,       d
            start               cur
     pre=none       cur
                  b->none, pre   cur
                               c-> b, pre    cur
                 b-> cur(d)    a-> pre(c)


        08/04/2022 12:00	Accepted	4646 ms	91.6 MB	python
        medium
        30-60mins
        linked list o(1) space
        o(n) space can store the list node to array and reverse them.
        """
        start = head
        d = 2
        while start.next:
            cur, n = start, 0
            # get count for each group
            for _ in range(d):
                if not cur.next:
                    break
                n += 1
                cur = cur.next

            if n % 2 == 1: # odd
                start = cur
            else:  # even and let's reverse it
                cur, pre = start.next, None   # set cur point to the start of group
                for _ in range(n):
                    cur.next, cur, pre = pre, cur.next, cur  # this one line to avoid extra variable post, equals below
                    # post = cur.next
                    # cur.next = pre
                    # pre = cur
                    # cur = post

                start.next.next, start.next, start = cur, pre, start.next
            d += 1
        return head
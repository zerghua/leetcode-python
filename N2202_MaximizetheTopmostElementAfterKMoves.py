#
# Create by Hua on 7/21/22
#

"""
You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.



Example 1:

Input: nums = [5,2,2,4,0,6], k = 4
Output: 5
Explanation:
One of the ways we can end with 5 at the top of the pile after 4 moves is as follows:
- Step 1: Remove the topmost element = 5. The pile becomes [2,2,4,0,6].
- Step 2: Remove the topmost element = 2. The pile becomes [2,4,0,6].
- Step 3: Remove the topmost element = 2. The pile becomes [4,0,6].
- Step 4: Add 5 back onto the pile. The pile becomes [5,4,0,6].
Note that this is not the only way to end with 5 at the top of the pile. It can be shown that 5 is the largest answer possible after 4 moves.
Example 2:

Input: nums = [2], k = 1
Output: -1
Explanation:
In the first move, our only option is to pop the topmost element of the pile.
Since it is not possible to obtain a non-empty pile after one move, we return -1.


Constraints:

1 <= nums.length <= 105
0 <= nums[i], k <= 109

"""


class Solution(object):
    def maximumTop(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        thought:
        k==0, return a[0] or -1 if len(a) == 0
        k==1, return a[1] or -1 if len(a) <= 1
        k>=2, -1 if len(a) == 0

        [1,2,3,4], k=2, k=4, k =5,6
        0,1,2,3
        1) k < len(a)
        1. remove k elements, return a[k]
        2. remove k-1 elements, pick the max from a[:k-1] return max(a[:k-1])
        3. can never return a[k-1]

        # can't pick the last one, a[k-1]
        2) k == len(a)
            return max(a[:k-1])

        [1,2] k = 3, remove(1,2), add(2)
        [1,2] k = 4, remove(1,2), add(1,2)
        [1,2] k = 5, remove(1,2), add(1,2), remove(1)
        [1,2] k = 6, remove(1,2), add(1,2), remove(2), add(2)

        # corner case
        [3], k = 1, remove(3), return -1
        [3], k = 2, remove(3), add(3), return 3
        [3], k = 3, remove(3), add(3), remove(3), return -1

        3) k > len(a);
            return max(a)

        07/21/2022 11:44	Accepted	850 ms	24.2 MB	python
        medium, many cases
        30-40 min
        """
        n =len(nums)
        if k == 0:
            return -1 if n == 0 else nums[0]

        if k == 1:
            return -1 if n <= 1 else nums[1]

        if n == 0:
            return -1

        if n == 1:
            return -1 if k % 2 == 0 else nums[0]

        if k < n:
            return max(nums[k], max(nums[:k-1]))
        elif k == n:
            return max(nums[:k-1])
        else:
            return max(nums)




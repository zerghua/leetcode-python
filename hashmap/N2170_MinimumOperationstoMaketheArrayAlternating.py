#
# Create by Hua on 7/24/22
#

"""
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.



Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations.
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105

"""


class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: count frequency for odd and even numbers, use most_common(2) get to the top 2 num,
        if odd1 != even1, then return (len(odd) - odd1_count) + (len(even) - even1_count)
        else: min((len(odd) - odd1_count) + (len(even) - even2_count),  (len(odd) - odd2_count) + (len(even) - even1_count))

        07/24/2022 10:48	Accepted	2207 ms	28.9 MB	python
        medium 30-40min
        many corner cases.
        hashtable
        """
        if len(nums) == 1:
            return 0

        even, odd = nums[0::2], nums[1::2]
        even_size, odd_size = len(even), len(odd)
        import collections
        even_dt, odd_dt = collections.Counter(even).most_common(2), collections.Counter(odd).most_common(2)


        if even_dt[0][0] != odd_dt[0][0]:
            return (even_size - even_dt[0][1]) + (odd_size - odd_dt[0][1])
        else:
            # corner cases, most count num in odd and even are equal
            # [1,1,1], return 1
            if len(even_dt) == 1 and len(odd_dt) == 1:
                return min(even_dt[0][1], odd_dt[0][1])

            # # [1,1,3], return 0
            if len(even_dt) == 1:
                return odd_size - odd_dt[1][1]

            if len(odd_dt) == 1:
                return even_size - even_dt[1][1]

            # now both odd_dt and even_dt == 2
            # additional corner case:
            # [4, 3, 4, 3, 4, 3, 3, 5, 3, 5, 3, 3]
            # [(3, 3), (4, 3)]
            # [(3, 4), (5, 2)]
            return min((even_size - even_dt[1][1]) + (odd_size - odd_dt[0][1]), (even_size - even_dt[0][1]) + (odd_size - odd_dt[1][1]))


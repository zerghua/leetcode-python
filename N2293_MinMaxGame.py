#
# Create by Hua on 7/12/22
#

"""
You are given a 0-indexed integer array nums whose length is a power of 2.

Apply the following algorithm on nums:

Let n be the length of nums. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n / 2.
For every even index i where 0 <= i < n / 2, assign the value of newNums[i] as min(nums[2 * i], nums[2 * i + 1]).
For every odd index i where 0 <= i < n / 2, assign the value of newNums[i] as max(nums[2 * i], nums[2 * i + 1]).
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the last number that remains in nums after applying the algorithm.



Example 1:


Input: nums = [1,3,5,2,4,8,2,2]
Output: 1
Explanation: The following arrays are the results of applying the algorithm repeatedly.
First: nums = [1,5,4,2]
Second: nums = [1,4]
Third: nums = [1]
1 is the last remaining number, so we return 1.
Example 2:

Input: nums = [3]
Output: 3
Explanation: 3 is already the last remaining number, so we return 3.


Constraints:

1 <= nums.length <= 1024
1 <= nums[i] <= 109
nums.length is a power of 2.

"""


class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        thought: simulate the problem.
        07/12/2022 16:46	Accepted	82 ms	13.8 MB	python
        easy 5-10 min
        """

        ret = nums
        while len(ret) != 1:
            tmp = list()
            odd = True
            for i in range(len(ret)/2):
                if odd:
                    tmp.append(min(ret[i*2], ret[i*2+1]))
                else:
                    tmp.append(max(ret[i*2], ret[i*2+1]))
                odd = not odd
            ret = tmp

        return ret[0]

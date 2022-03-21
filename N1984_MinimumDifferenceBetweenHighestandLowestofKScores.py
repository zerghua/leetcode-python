#
# Create by Hua on 2/1/22.
#

"""
You are given a 0-indexed integer array nums, where nums[i] represents the
score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference
between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.


Example 1:

Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:

Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.



Constraints:

    1 <= k <= nums.length <= 1000
    0 <= nums[i] <= 105


"""


class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        slidng window math problem.

        thought: problem description is not very straightforward, basically,
        it's asking to find k numbers in an array which has the minimum
        difference.
        so, sort the array, and sliding window to find the minimum
        difference in the k numbers window.

        easy - medium, spend 10-20 min to think through.
        wrong answer when thought: (and k is useless when larger
        than 2, because we are only comparing the adjacent 2 numbers.)

        the question is to find the difference between n[i] and n[i-k+1]
        in a sliding window of k

        Input: [87063,61094,44530,21297,95857,93551,9918]
        9918,21297,44530,61094,87063,93551,95857
        6
        Output: 2306
        Expected: 74560

        k = 3
        i = 3 - 3 + 1

        03/21/2022 10:46	Accepted	85 ms	13.5 MB	python
        """
        n = len(nums)
        if k == 1 or n <= 1: return 0
        sorted_num = sorted(nums)
        ret = sorted_num[k-1] - sorted_num[0]
        for i in range(k, n):
            ret = min(ret, sorted_num[i] - sorted_num[i-k+1])
        return ret


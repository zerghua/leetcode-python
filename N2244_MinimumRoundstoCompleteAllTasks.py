#
# Create by Hua on 7/15/22
#

"""
You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.



Example 1:

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2.
- In the second round, you complete 2 tasks of difficulty level 3.
- In the third round, you complete 3 tasks of difficulty level 4.
- In the fourth round, you complete 2 tasks of difficulty level 4.
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
Example 2:

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.


Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109

"""


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int

        thought: more of a math, to find the pattern. hashmap all num first.
        1, return -1
        2, return 1
        3, return 1
        4, 4%3 ~ 1(not a go), 4/2 = 2 return 2
        5, return 2, 5%3 ~ 2, 3+2
        6, return 2, 6%3 ~ 0
        7, return 3, 7%3 ~ 1(not a go, but decrease one, make it 3 + 4)
        8, return 3, (2*3)+ 2

        07/15/2022 10:34	Accepted	1124 ms	26.5 MB	python
        medium - easy. math.
        10-20 min.
        """

        import collections
        dt = collections.Counter(tasks)

        ret = 0
        for v in dt.values():
            if v == 1: return -1
            if v <= 3: ret += 1
            else:
                if v % 3 == 0:
                    ret += v/3
                else: # include both v%3 = 1 or 2
                    ret += v/3 + 1

        return ret

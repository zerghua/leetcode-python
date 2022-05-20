#
# Create by Hua on 5/20/22
#


"""
You are given two strings current and correct representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

Return the minimum number of operations needed to convert current to correct.



Example 1:

Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
We can convert current to correct in 3 operations as follows:
- Add 60 minutes to current. current becomes "03:30".
- Add 60 minutes to current. current becomes "04:30".
- Add 5 minutes to current. current becomes "04:35".
It can be proven that it is not possible to convert current to correct in fewer than 3 operations.
Example 2:

Input: current = "11:00", correct = "11:01"
Output: 1
Explanation: We only have to add one minute to current, so the minimum number of operations needed is 1.


Constraints:

current and correct are in the format "HH:MM"
current <= correct

"""


class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int

        thought: calculate minute difference between correct and current,
        corner case of 2 ways, like  11:00, 11:10  and 11:00, 10:50
        we can convert both time to minutes. (hh*60 + mm) and do a abs(a-b)
        then we greedy pick [60,15,5,1] to meet the diff.

        05/20/2022 11:46	Accepted	27 ms	13.6 MB	python
        easy 5min.

        others code:
        class Solution:
            def convertTime(self, current: str, correct: str) -> int:
                current_time = 60 * int(current[0:2]) + int(current[3:5]) # Current time in minutes
                target_time = 60 * int(correct[0:2]) + int(correct[3:5]) # Target time in minutes
                diff = target_time - current_time # Difference b/w current and target times in minutes
                count = 0 # Required number of operations
                # Use GREEDY APPROACH to calculate number of operations
                for i in [60, 15, 5, 1]:
                    count += diff // i # add number of operations needed with i to count
                    diff %= i # Diff becomes modulo of diff with i
                return count
        """
        a = int(current.split(":")[0]) * 60 + int(current.split(":")[1])
        b = int(correct.split(":")[0]) * 60 + int(correct.split(":")[1])
        diff = abs(a-b)
        ret = 0
        change = [60,15,5,1]
        while diff:
            for c in change:
                if diff >= c:
                    diff -= c
                    ret += 1
                    break
        return ret





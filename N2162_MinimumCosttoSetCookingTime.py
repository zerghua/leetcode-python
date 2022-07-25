#
# Create by Hua on 7/25/22
#

"""
A generic microwave supports cooking times for:

at least 1 second.
at most 99 minutes and 99 seconds.
To set the cooking time, you push at most four digits. The microwave normalizes what you push as four digits by prepending zeroes. It interprets the first two digits as the minutes and the last two digits as the seconds. It then adds them up as the cooking time. For example,

You push 9 5 4 (three digits). It is normalized as 0954 and interpreted as 9 minutes and 54 seconds.
You push 0 0 0 8 (four digits). It is interpreted as 0 minutes and 8 seconds.
You push 8 0 9 0. It is interpreted as 80 minutes and 90 seconds.
You push 8 1 3 0. It is interpreted as 81 minutes and 30 seconds.
You are given integers startAt, moveCost, pushCost, and targetSeconds. Initially, your finger is on the digit startAt. Moving the finger above any specific digit costs moveCost units of fatigue. Pushing the digit below the finger once costs pushCost units of fatigue.

There can be multiple ways to set the microwave to cook for targetSeconds seconds but you are interested in the way with the minimum cost.

Return the minimum cost to set targetSeconds seconds of cooking time.

Remember that one minute consists of 60 seconds.


Example 1:


Input: startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600
Output: 6
Explanation: The following are the possible ways to set the cooking time.
- 1 0 0 0, interpreted as 10 minutes and 0 seconds.
  The finger is already on digit 1, pushes 1 (with cost 1), moves to 0 (with cost 2), pushes 0 (with cost 1), pushes 0 (with cost 1), and pushes 0 (with cost 1).
  The cost is: 1 + 2 + 1 + 1 + 1 = 6. This is the minimum cost.
- 0 9 6 0, interpreted as 9 minutes and 60 seconds. That is also 600 seconds.
  The finger moves to 0 (with cost 2), pushes 0 (with cost 1), moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).
  The cost is: 2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 12.
- 9 6 0, normalized as 0960 and interpreted as 9 minutes and 60 seconds.
  The finger moves to 9 (with cost 2), pushes 9 (with cost 1), moves to 6 (with cost 2), pushes 6 (with cost 1), moves to 0 (with cost 2), and pushes 0 (with cost 1).
  The cost is: 2 + 1 + 2 + 1 + 2 + 1 = 9.
Example 2:


Input: startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76
Output: 6
Explanation: The optimal way is to push two digits: 7 6, interpreted as 76 seconds.
The finger moves to 7 (with cost 1), pushes 7 (with cost 2), moves to 6 (with cost 1), and pushes 6 (with cost 2). The total cost is: 1 + 2 + 1 + 2 = 6
Note other possible ways are 0076, 076, 0116, and 116, but none of them produces the minimum cost.


Constraints:

0 <= startAt <= 9
1 <= moveCost, pushCost <= 105
1 <= targetSeconds <= 6039

"""


class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int

        thought: time range from 1s to 6039s(converted to 99m, 99s), target is given in seconds,
        so we need to convert it to mm, ss,
        if targetSeconds < 60: (e.g 48), move to 4 and 8, push once for both
        if targetSeconds == 60, it can be below, pick the min val:
            1: 1mm, 00s; move to 1 and 0, push 1 once, push 0 twice.
            2. 60s; move to 6 and 0, push 6 and push 0 once.
        if n in  [61, 99]:
            1. push 61-99,
            2. push 1m, n-60
        if n >= 100:
            1. push r = n%60, push  n - r*60 (e.g 100 -> 1m,40s,   120 -> 2m or 1m,60s, 200 -> 3m,20s or 2m,80s)
            or could try let n -60 to convert to m for multiple times, until n is between [59,99]
            or m = n % 60, s = n - 60*m, if s < 40, another form is m - 1, s = s+60, if m == 0 can be skipped.
            if m == 0 and s <10, only to to push 1 digit

        need to sort out the various cases, take some time

        algorithm:
            1. convert the target seconds to valid minimal forms
            2. calculate each valid forms val
            3. return the min val

        a corner case, m also needs to be less than 100
        07/25/2022 10:47	Accepted	35 ms	13.3 MB	python
        medium, coding didn't take much time, but the analysis, take over 30min.
        40-50 min.
        """
        def get_cost(m, s):
            if m < 0 or m > 99 or s < 0 or s >99:
                return 10**9
            if m == 0:
                digit = str(s)  #5, 12
            else:
                digit = str(m) + str(s) if s >=10 else str(m) + "0" + str(s)   # 1:05, 1:25, actual is 105, 125, 122

            pre = ""
            cost = pushCost * len(digit)
            if digit[0] == str(startAt):
                cost -= moveCost
            for c in digit:
                if c != pre:
                    cost += moveCost
                pre = c
            return cost


        m = targetSeconds / 60
        s = targetSeconds - m * 60
        return min(get_cost(m,s), get_cost(m-1, s+60))




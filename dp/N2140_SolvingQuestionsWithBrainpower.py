#
# Create by Hua on 7/26/22
#

"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.



Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
Example 2:

Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.


Constraints:

1 <= questions.length <= 105
questions[i].length == 2
1 <= pointsi, brainpoweri <= 105

"""


class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int

        thought: dp. either choose or skip.
        [[3,2],[4,3],[4,4],[2,5]]
        0, 1, 2, 3

        choose 0, or not
        return max(dp[i] + dfs(i+power+1), dp[i+1])

        https://leetcode.com/problems/solving-questions-with-brainpower/discuss/1692963/DP
            Take: points[i] + dp[i + 1 + brainpower[i]],
            Skip: dp[i + 1].

        it's much easier to code when scan from right to left
        07/26/2022 10:27	Accepted	1708 ms	65.2 MB	python
        medium. almost figure out, was thinking to scan from left to right, which is much harder.
        30-40min.
        """
        dp = [0] * (2*10**5 + 1)   # avoid length checking
        for i in range(len(questions)-1, -1, -1):
            point = questions[i][0]
            power = questions[i][1]
            dp[i] = max(dp[i+1], point + dp[i+1+power])
        return dp[0]







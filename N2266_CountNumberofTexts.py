#
# Create by Hua on 5/28/22.
#

"""
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.

In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

    For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
    Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.

However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

    For example, when Alice sent the message "bob", Bob received the string "2266622".

Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.

Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.



Constraints:

    1 <= pressedKeys.length <= 105
    pressedKeys only consists of digits from '2' - '9'.


"""


class Solution(object):
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int

        thought: math, combinations. only 7 and 9 can press 4 times,
        other at most 3 times.
        2 =      1  [a]
        2(2) =   2  [aa, (b)]
        2(22) =  4  [dp1(ab), dp2(aaa, ba), (c)]
        2(222) = 7  [dp1(ac),dp2(aab, bb),dp3(aba,aaaa,baa,ca)]
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] (when they are the same)

        https://leetcode.com/problems/count-number-of-texts/discuss/2018336/Python-or-DP-with-diagrams-for-beginners

        05/28/2022 12:32	Accepted	661 ms	21.5 MB	python
        medium - hard. if can't work out the math(dp), can't solve it.
        60-90 min.
        """
        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1
        mod = 10**9 + 7
        for i in range(1, len(pressedKeys)+1):
            dp[i] = dp[i-1] % mod
            if i >= 2 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] = (dp[i] + dp[i-2]) % mod
                if i >= 3 and pressedKeys[i-1] == pressedKeys[i-3]:
                    dp[i] = (dp[i] + dp[i - 3]) % mod
                    if i>=4 and pressedKeys[i-1] == pressedKeys[i-4] and pressedKeys[i-1] in '79':
                        dp[i] = (dp[i] + dp[i - 4]) % mod

        return dp[-1]
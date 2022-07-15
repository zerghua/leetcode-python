#
# Create by Hua on 7/15/22
#

"""
You are given a 0-indexed string expression of the form "<num1>+<num2>" where <num1> and <num2> represent positive integers.

Add a pair of parentheses to expression such that after the addition of parentheses, expression is a valid mathematical expression and evaluates to the smallest possible value. The left parenthesis must be added to the left of '+' and the right parenthesis must be added to the right of '+'.

Return expression after adding a pair of parentheses such that expression evaluates to the smallest possible value. If there are multiple answers that yield the same result, return any of them.

The input has been generated such that the original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.



Example 1:

Input: expression = "247+38"
Output: "2(47+38)"
Explanation: The expression evaluates to 2 * (47 + 38) = 2 * 85 = 170.
Note that "2(4)7+38" is invalid because the right parenthesis must be to the right of the '+'.
It can be shown that 170 is the smallest possible value.
Example 2:

Input: expression = "12+34"
Output: "1(2+3)4"
Explanation: The expression evaluates to 1 * (2 + 3) * 4 = 1 * 5 * 4 = 20.
Example 3:

Input: expression = "999+999"
Output: "(999+999)"
Explanation: The expression evaluates to 999 + 999 = 1998.


Constraints:

3 <= expression.length <= 10
expression consists of digits from '1' to '9' and '+'.
expression starts and ends with digits.
expression contains exactly one '+'.
The original value of expression, and the value of expression after adding any pair of parentheses that meets the requirements fits within a signed 32-bit integer.

"""


class Solution(object):
    def minimizeResult(self, expression):
        """
        :type expression: str
        :rtype: str

        thought: the length of the expression is short, so we try all possible combinations.
        a * (b + c) *d , corner case, a and d might not exist, use 1
        12+34

        tricky code.
        medium 10-20 min
        07/15/2022 16:11	Accepted	23 ms	13.6 MB	python
        """

        ls = expression.split("+")
        x, y = ls[0], ls[1]
        ret = ""
        total = 2**31 - 1
        for i in range(len(x)):
            for j in range(1, len(y)+1):
                a = 1 if i == 0 else int(x[:i])
                b = int(x[i:])
                c = int(y[:j])
                d = 1 if j == len(y) else int(y[j:])
                t = a * (b+c) * d
                if t <= total:
                    total = t
                    ret = x[:i] + "(" + x[i:] + "+" + y[:j] + ")" + y[j:]

        return ret


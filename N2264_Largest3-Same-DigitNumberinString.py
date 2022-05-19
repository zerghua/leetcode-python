#
# Create by Hua on 5/19/22
#


"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.


Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.


Constraints:

3 <= num.length <= 1000
num only consists of digits.

"""


class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str

        thought: sliding window of size 3 string, check if they are the same and return the largest
        05/19/2022 10:30	Accepted	18 ms	13.5 MB	python
        easy 5 min.
        """
        n = len(num)
        ret = ""
        for i in range(n-2):
            a = num[i:i+3]
            if a[0] == a[1] == a[2]:
                if not ret or int(a) > int(ret):
                    ret = a
        return ret

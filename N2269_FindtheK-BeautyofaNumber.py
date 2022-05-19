#
# Create by Hua on 5/19/22
#


"""
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.



Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.


Constraints:

1 <= num <= 109
1 <= k <= num.length (taking num as a string)

"""


class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int

        thought: convert from string to int and corner case of 0
        05/19/2022 10:23	Accepted	32 ms	13.4 MB	python
        easy 5-10 min.
        """
        s = list(str(num))
        ret = 0
        for i in range(len(s) - k + 1):
            i = int("".join(s[i:i+k]))
            if i != 0 and num % i == 0:
                ret += 1
        return ret

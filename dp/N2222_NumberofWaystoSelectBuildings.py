#
# Create by Hua on 7/18/22
#

"""
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.



Example 1:

Input: s = "001101"
Output: 6
Explanation:
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.


Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.

"""


class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int

        thought: BF will be o(n^3), dp is o(n)
        didn't figure out how to model dp.
        https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/1907109/PythonDP-easy-to-understand

        When you meet a "0", you can possibly form "0", "10", "010" ending with a "0".
        When you meet a "1", you can possibly form "1", "01", "101" ending with a "1".
        Update the number of possible combinations when you traverse s.

        07/18/2022 11:20	Accepted	1015 ms	15 MB	python
        medium. dp. didn't figure out the model.

        """

        dp = {"0":0, "01":0, "010":0, "1":0, "10":0, "101":0}
        for n in s:
            if n == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            else:
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]

        return dp["101"] + dp["010"]

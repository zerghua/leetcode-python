#
# Create by Hua on 7/25/22
#

"""
You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
[5, 6, 3, 7] is not possible since it contains an element greater than 6.
[1, 2, 3, 4] is not possible since the differences are not correct.
Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.



Example 1:

Input: differences = [1,-3,4], lower = 1, upper = 6
Output: 2
Explanation: The possible hidden sequences are:
- [3, 4, 1, 5]
- [4, 5, 2, 6]
Thus, we return 2.
Example 2:

Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
Output: 4
Explanation: The possible hidden sequences are:
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
Thus, we return 4.
Example 3:

Input: differences = [4,-7,2], lower = 3, upper = 6
Output: 0
Explanation: There are no possible hidden sequences. Thus, we return 0.


Constraints:

n == differences.length
1 <= n <= 105
-105 <= differences[i] <= 105
-105 <= lower <= upper <= 105

"""


class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int

        thought: from hints
        Fix the first element of the hidden sequence to any value x and ignore the given bounds.
        Notice that we can then determine all the other elements of the sequence by using the differences array.

        We will also be able to determine the difference between the minimum and maximum elements of the sequence.
        Notice that the value of x does not affect this.

        We now have the ‘range’ of the sequence (difference between min and max element),
        we can then calculate how many ways there are to fit this range into the given range of lower to upper.

        Answer is (upper - lower + 1) - (range of sequence)

        07/25/2022 15:23	Accepted	1013 ms	25.4 MB	python
        medium, more like a brain teaser.
        didn't figure out myself, got solution from hints.

        """

        ret = [1]
        for n in differences:
            ret.append(ret[-1] + n)

        ret = (upper - lower + 1) - (max(ret) - min(ret))
        return ret if ret > 0 else 0

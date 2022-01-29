#
#  Create by Hua on 1/29/2022
#

"""
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

    The integer consists of the concatenation of three elements from digits in any arbitrary order.
    The integer does not have leading zeros.
    The integer is even.

For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.


Example 1:
Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.

Example 2:
Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.

Example 3:
Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.



Constraints:

    3 <= digits.length <= 100
    0 <= digits[i] <= 9

"""


class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        easy: 10 min, o(n^3) loops, used set and list.

        thought: o(n^3) solution? 3 loops to test all possible combinations, store result in set or list(make sure
        it's unique)

        01/29/2022 14:20	Accepted	7329 ms	13.5 MB	python


        """

        i=j=k=0
        n = len(digits)
        ret = set()
        for i in range(n):
            if digits[i] == 0: continue
            for j in range(n):
                if j == i: continue
                for k in range(n):
                    if k == i or k == j: continue
                    num = 100*digits[i] + 10*digits[j] + digits[k]
                    if num %2 == 0:
                        ret.add(num)

        return list(sorted(ret))

    def findEvenNumbers_withhint(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        used 10-15 min, stuck on "num = int(c)", forgot to convert char to int, hence it can't find it in int list.

        hint:
        The range of possible answers includes all even numbers between 100 and 999 inclusive.
        Could you check each possible answer to see if it could be formed from the digits in the array?

        01/29/2022 14:49	Accepted	84 ms	13.4 MB	python (much faster solution) o(n)
        """

        ret = list()
        for i in range(100,999,2):
            s = str(i)
            lst = list(digits)
            for c in s:
                num = int(c)
                if num in lst:
                    lst.remove(num)
                else:
                    break

            if len(lst) + 3 == len(digits):
                ret.append(i)

        return sorted(ret)
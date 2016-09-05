#
# Created by Hua on 9/4/2016
#

"""
 Given two numbers represented as strings, return multiplication of the numbers as a string.

 Note:

 The numbers can be arbitrarily large and are non-negative.
 Converting the input string to integer is NOT allowed.
 You should NOT use internal library such as BigInteger.
"""

# 359 ms
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_size, num2_size = len(num1), len(num2)
        ret = [0]* (num1_size + num2_size)
        for i in range(num1_size-1, -1, -1):
            for j in range(num2_size-1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                p1 = i+j
                p2 = i+j+1
                sum_with_carry = product + ret[p2]  #  i.e 35 + 6 = 41
                ret[p1] += sum_with_carry / 10;     #  4
                ret[p2] = sum_with_carry % 10;      #  6 --> 1

        ret_str = ''.join(str(i) for i in ret).lstrip('0')
        return ret_str if len(ret_str) != 0 else "0"


print Solution().multiply("123", "45")
print Solution().multiply("0", "0")
print Solution().multiply("123", "0")

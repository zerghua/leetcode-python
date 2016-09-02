#
#  Create by Hua on 9/2/2016
#


"""
 The count-and-say sequence is the sequence of integers beginning as follows:
 1, 11, 21, 1211, 111221, ...

 1 is read off as "one 1" or 11.
 11 is read off as "two 1s" or 21.
 21 is read off as "one 2, then one 1" or 1211.

 Given an integer n, generate the nth sequence.

 1-->1
 2-->11
 3-->21
 4-->1211
 5-->111221
 6-->312211
 7-->13112221

"""

# this one is hard on how to understand the problem and translate it to code.
# 59 ms  18 / 18 test cases passed.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<0: return "";
        ret= "1"
        count = 1
        for i in range(1,n):
            next_str = ""
            for j in range(len(ret)):
                if j < len(ret)-1 and ret[j] == ret[j+1]:
                    count += 1
                else:
                    next_str += str(count) + ret[j]
                    count = 1
            ret = next_str
        return ret


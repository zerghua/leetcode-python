#
#  Create by Hua on 9/1/2016
#


"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

"""


# 64ms  72 / 72 test cases passed.
# brute force o(m*n)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        haystack_size = len(haystack)
        needle_size = len(needle)

        if haystack is None or needle is None: return -1
        if needle_size == 0: return 0
        if haystack_size == 0: return -1

        i = j = 0
        while i< haystack_size and j< needle_size:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i-j+1
                j=0

        if j == needle_size: return i-j
        return -1


# 164 ms  72 / 72 test cases passed.
# KMP is slower than brute force?
class Solution2(object):

    def get_next_array(self, needle):
        n = len(needle)
        a = [0] * n
        a[0] = -1
        j=0
        k=-1
        while j< n-1:
            if k==-1 or needle[j] == needle[k]:
                j += 1
                k += 1
                if needle[j] == needle[k]: a[j] = a[k]
                else: a[j] = k
            else:
                k = a[k]
        return a


    def strStr(self, haystack, needle):
        haystack_size = len(haystack)
        needle_size = len(needle)

        if haystack is None or needle is None: return -1
        if needle_size == 0: return 0
        if haystack_size == 0: return -1

        i = j = 0
        next_array = self.get_next_array(needle)
        while i< haystack_size and j< needle_size:
            if j==-1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_array[j]

        if j == needle_size: return i-j
        return -1
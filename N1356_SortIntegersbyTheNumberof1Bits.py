#
# Create by Hua on 4/7/22.
#

"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.



Example 1:

Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.



Constraints:

    1 <= arr.length <= 500
    0 <= arr[i] <= 104


"""


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        thought: sort arr, check put them into 20 buckets of list, each bucket
        represent number of 1's
        04/07/2022 14:50	Accepted	61 ms	13.7 MB	python
        easy 5-10 min. some python syntax. extend to extend list.
        how to initialize list of list.
        or simplified code with custom sort.
        """
        a = sorted(arr)
        b = [[] for i in range(20)]
        for i in a:
            x = int(bin(i).count("1"))
            b[x].append(i)
        ret = list()
        for i in range(20):
            if len(b[i]) > 0:
                ret.extend(b[i])
        return ret

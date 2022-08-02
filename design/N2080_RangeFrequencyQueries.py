#
# Create by Hua on 8/2/22
#

"""
Design a data structure to find the frequency of a given value in a given subarray.

The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the RangeFreqQuery class:

RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).



Example 1:

Input
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
Output
[null, 1, 2]

Explanation
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.


Constraints:

1 <= arr.length <= 105
1 <= arr[i], value <= 104
0 <= left <= right < arr.length
At most 105 calls will be made to query

"""
import collections
import bisect

class RangeFreqQuery(object):
    import collections
    def __init__(self, arr):
        """
        :type arr: List[int]
            thought: a hashmap to store a value's (index), use a binary search for the ranged count

            a = [2,5,8]
            bisect.bisect_left(a,1)   0
            bisect.bisect_left(a,3)   1
            bisect.bisect_left(a,5)   1
            bisect.bisect_left(a,6)   2
            bisect.bisect_left(a,8)   2 , lower range should bisect_left
            bisect.bisect_right(a,8)  3 , upper range should use bisect_right
            [5,8], should return 2
            [6,8], should return 1

            08/02/2022 15:18	Accepted	1955 ms	53.7 MB	python
            medium.
            binary search + hashmap.
            20-30min.

        """
        self.dt = collections.defaultdict(list)
        for i in range(len(arr)):
            self.dt[arr[i]].append(i)

    def query(self, left, right, value):
        """
        :type left: int
        :type right: int
        :type value: int
        :rtype: int
        """
        if value not in self.dt:
            return 0
        
        a = self.dt[value]  # list of index
        return bisect.bisect_right(a, right) - bisect.bisect_left(a,left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
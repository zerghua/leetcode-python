#
# Create by Hua on 7/27/22
#

"""
You are given a 0-indexed array of n integers arr.

The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.

Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].

Note: |x| is the absolute value of x.



Example 1:

Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]
Explanation:
- Index 0: Another 2 is found at index 4. |0 - 4| = 4
- Index 1: Another 1 is found at index 3. |1 - 3| = 2
- Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
- Index 3: Another 1 is found at index 1. |3 - 1| = 2
- Index 4: Another 2 is found at index 0. |4 - 0| = 4
- Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
- Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
Example 2:

Input: arr = [10,5,10,10]
Output: [5,0,3,4]
Explanation:
- Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
- Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
- Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
- Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4


Constraints:

n == arr.length
1 <= n <= 105
1 <= arr[i] <= 105

"""


class Solution(object):
    def getDistances(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        thought: hashmap and prefix sum.
        3,5,6,8
        |3-5| + |3-6| + |3-8| = 2+3+5 = 10
        |5-3| + |5-6| + |5-8| = 2+1+3 = 6
        |6-3| + |6-5| + |6-8| = 3+1+2 = 6
        |8-3| + |8-5| + |8-6| = 5+3+2 = 10

        1,2, x,y, n
        (x-1) + (x-2) + (y-x) +  (n-x)  == a
        (y-1) + (y-2) + (y-x) +  (n-y)  == b
        b - a = (y -x) + (y-x) + ... (x-y)
        b - a = 2*(y-x) + 1*(x-y)
        b = a + 2*(y-x) + 1*(x-y)  (m is pre x count, n is after y count)  this is the formula

        3,5,6,8
        10
        = 10 + 0*(5-3) + (4-2)*(3-5) = 10 + (-4) = 6
        = 6 + 1*(6-5) + 1*(5-6) = 6 + 1 - 1 = 6
        = 6 + 2*(8-6) + 0 = 10


        07/27/2022 10:01	Accepted	4575 ms	58 MB	python
        medium
        take 30-40 min to find the prefix formula,
        total 50-60min.
        prefix sum + hashmap
        """
        import collections
        dt, ret = collections.defaultdict(list), collections.defaultdict(list)
        for i in range(len(arr)):  # put each duplicate number into a list
            dt[arr[i]].append(i)

        for key in dt.keys():  # for each list, we calculate it's sum of distance and put it into ret
            lt = dt[key]
            n = len(lt)
            if n == 1:
                ret[key].append(0)
                continue

            # n > 1, calculate the first sum of distance
            total = 0
            for num in lt:
                total += abs(num - lt[0])
            ret[key].append(total)

            # b = a + (i-1)(y-x) + (n-i-1)*(x-y)
            #   = a + iy - ix -y + x + nx - ix - x - ny + iy + y
            #   = a + 2iy - 2ix + nx - ny
            #   = a + 2i(y-x) + n(x-y)
            for i in range(1, n):
                t = ret[key][-1] + (i-1)*(lt[i] - lt[i-1]) + (n-i-1)*(lt[i-1] - lt[i])
                ret[key].append(t)

        ans = list()
        for n in arr:
            ans.append(ret[n].pop(0))

        return ans






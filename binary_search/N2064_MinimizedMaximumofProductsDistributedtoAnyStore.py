#
# Create by Hua on 8/5/22
#

"""
You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.



Example 1:

Input: n = 6, quantities = [11,6]
Output: 3
Explanation: One optimal way is:
- The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
- The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.
Example 2:

Input: n = 7, quantities = [15,10,10]
Output: 5
Explanation: One optimal way is:
- The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
- The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
- The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.
Example 3:

Input: n = 1, quantities = [100000]
Output: 100000
Explanation: The only optimal way is:
- The 100000 products of type 0 are distributed to the only store.
The maximum number of products given to any store is max(100000) = 100000.


Constraints:

m == quantities.length
1 <= m <= n <= 105
1 <= quantities[i] <= 105

"""


class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        thought: binary search a satisfying mid.
        n = 6, quantities = [11,6]
        return 3

        when mid == 4,
        total = ceil(11/4) + ceil(6/4) = 5  <= n(6), (can distribute to 5 or more stores, this mid is ok)
        right = mid

        when mid == 2,
        total = ceil(11/2) + ceil(6/2) = 9 > n(n)  (can't distribute all products to stores, need at least 9 stores)
        left = mid + 1

        left = 3, right =4
        when mid == 3,
        total = ceil(11/3) + ceil(6/3) = 6 <= n(6)
        right = 3, left = 3, break


        left = 2, right = 4,
        -> mid =3, left=2, right=3,
        -> mid =2, left=3, right=3  break

        1. left,  mid ,  right
        2. left,  right  or
                       left, right
        if it's a good mid, right will set to mid and be closer to left,
        else: left = mid + 1, also it's moving closer to right, eventually they will be equal

        7
        [15,10,10]
        k = 4
        4,4,4,3, 4,4,2, 4,4,2

        08/05/2022 15:37	Accepted	2920 ms	24.1 MB	python
        medium
        30-40 min
        binary search
        also learned python 2.x has issue in math.ceil(x/y), need to float the x or y
        """
        import math
        left, right = 1, max(quantities)
        while left < right:
            fit_stores, mid = 0, (left + right)/2
            for x in quantities:
                fit_stores += math.ceil(float(x)/mid)  # math.ceil(x/mid) won't work in python 2.x, since it's truncating
            if fit_stores > n: # this is not a good mid
                left = mid + 1
            else:  # a good mid, but we want to keep trying to find the minimal mid
                right = mid
        return left

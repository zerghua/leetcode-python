#
# Create by Hua on 9/16/22
#

"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.



Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.
Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Constraints:

1 <= fruits.length <= 105
0 <= fruits[i] < fruits.length

"""


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int

        thought:
        maintain a non shrink sliding window.
        https://leetcode.com/problems/fruit-into-baskets/discuss/170740/JavaC%2B%2BPython-Sliding-Window-for-K-Elements

        09/16/2022 12:03	Accepted	2001 ms	19.7 MB	python
        """
        pre = j = 0
        n = len(fruits)
        dt={}
        while j < n:
            dt[fruits[j]] = dt.get(fruits[j],0) + 1
            if len(dt) > 2:  # here is a if rather than while
                dt[fruits[pre]]-=1
                if dt[fruits[pre]] == 0:
                    del dt[fruits[pre]]
                pre += 1
            j += 1
        return j - pre



class Solution_myself(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int

        thought: sliding window, need 2 pointers.
        use hashmap to contains the 2 types, when there are more than 2 types in the maps, we need to move forward
        the pre pointer and decrease the count in map until there is only 1 type in the map.

        coding could be a little bit tricky.

        BF solution is to check every point twice, leading to o(n^2) time

        however, sliding window is o(n) solution
        09/16/2022 11:48	Accepted	1626 ms	18.8 MB	python
        meiudm - easy
        20-30min
        sliding window + hashmap
        google, amazon, apple
        """
        import collections
        dt = collections.defaultdict(int)
        pre = 0
        n = len(fruits)
        ret = 0
        for i in range(n):
            dt[fruits[i]] += 1
            while len(dt) > 2:  # move left window
                dt[fruits[pre]]-=1
                if dt[fruits[pre]] == 0:
                    del dt[fruits[pre]]
                pre += 1
            ret = max(ret, sum(dt.values()))

        return ret




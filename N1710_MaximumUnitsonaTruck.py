#
# Create by Hua on 3/26/22.
#

"""
You are assigned to put some amount of boxes onto one truck. You are given
a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes
that can be put on the truck. You can choose any boxes to put on the truck as
long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.



Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91



Constraints:

    1 <= boxTypes.length <= 1000
    1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
    1 <= truckSize <= 106


"""


class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int

        thought: simple greedy, sort list of tuples of the second value
        decreasing, and pick as much box as you can
        03/26/2022 10:58	Accepted	123 ms	13.9 MB	python
        easy, 5min. had a bug.
        """
        boxTypes.sort(reverse=True, key=lambda x:x[1])
        ret = 0
        for b in boxTypes:
            if b[0] <= truckSize:
                ret += b[0] * b[1]
            else:
                ret += b[1] * truckSize
            truckSize -= b[0]
            if truckSize < 0: break
        return ret
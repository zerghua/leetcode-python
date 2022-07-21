#
# Create by Hua on 7/21/22
#

"""
There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:

When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
When a moving car collides with a stationary car, the number of collisions increases by 1.
After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.



Example 1:

Input: directions = "RLRSLL"
Output: 5
Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5.
Example 2:

Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.


Constraints:

1 <= directions.length <= 105
directions[i] is either 'L', 'R', or 'S'.

"""


class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int

        thought: brain teaser.
        from left to right, find the index of first S or R; as left_index
        from right to left, find the index of first S or L; as right_index
        between left_index and right_index(inclusive), count num of L and R which is the answer.
        right_index can be smaller than left_index, then it's answer is 0

        07/21/2022 09:04	Accepted	334 ms	18.2 MB	python
        medium - easy
        10-20 min. need to figure out how to calculate
        """

        left = right = -1
        n = len(directions)
        for i in range(n):
            if directions[i] in 'SR':
                left = i
                break

        for i in range(n-1,-1,-1):
            if directions[i] in 'SL':
                right = i
                break

        if left == -1 or right == -1:  # solve the case, LLLL or RRR
            return 0

        ret = 0
        for i in range(left, right+1):
            if directions[i] in "LR":
                ret += 1
        return ret


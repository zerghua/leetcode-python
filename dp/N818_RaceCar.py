#
# Create by Hua on 8/9/22
#

"""
Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.



Example 1:

Input: target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.
Example 2:

Input: target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.


Constraints:

1 <= target <= 10^4

"""


class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int

        company: google high frequency.
        thought: dp. give limit is 10^4, we are looking at o(n^2) dp solution
        pos:     0, 1, 3, 7, 15, 31, 63,
        speed:   1, 2, 4, 8, 16, 32, 64,
        min_step:0, 1, 2, 3, 4,  5,  6

                    2, 3, 5, 9
                    1, 2, 4, 8

        first pass we can get all min step for pos, 1,3,7,15 .. 2^n-1 == n  (all A)
        then second pass, each pos, 2, 6, 14, .. 2^n -2 == n+2   (extra RA)

        to reverse one pos, we need at 2 steps if current is A (RA), need 3 steps if current is R (ARA).
        to advance one pos, we need at 3 steps if current is A (RRA), need 2 steps if current is R (AA).

        for each pos, we try advance one(need extra 3),  and store all following min_steps after
        for each pos, we try reverse one(need extra 2),  and store all following min_steps before


        for reverse, first reverse will stop, but can speed to -1, then each A, will accelerate exponentially,
        speed as - or +(2^n),
        so speed is always going to be 1,2,4,8 .. 2^n or -1, -2, -4,.. -2^n

        reverse, 7,  6,  2,  2(reverse),3
                 -1, -2, -4, 1,         2


         pos    0,1,2,3,4,5,6,7
        0 steps   1   2       3
        1           4   5   5
        2                 7
        3
        0-1-3-2-3-5
          1 2 4 6 7
        so do we need direction on the i?
        the hard part is zip-zag, 1->3 ->2 ->3 ->5

        BFS + greedy, this can provide trace of operations, dp can't.
        hard
        08/09/2022 15:59	Accepted	52 ms	13.7 MB	python
        referred:  https://leetcode.com/problems/race-car/discuss/762584/Python-C%2B%2B-3-Simple-Steps-(BFS)
        3-4 hours. didn't figure out myself.
        """

        lt = [(0,0,1)]   # moves, pos, speed
        while lt:
            move, pos, speed = lt.pop(0)

            if pos == target:
                return move

            lt.append((move+1, pos+speed, speed*2))  # greedy on straight line

            # reverse only when moving away from target in the next move
            if (speed > 0 and pos + speed > target) or (speed < 0 and pos + speed < target):
                lt.append((move + 1, pos, - speed/ abs(speed)))

        return -1



class Solution(object):
    def racecar_with_track(self, target):
        """
        :type target: int
        :rtype: int        """

        lt = [(0,0,1, "")]   # moves, pos, speed, track
        while lt:
            move, pos, speed, track = lt.pop(0)

            if pos == target:
                print(track)
                return move

            lt.append((move+1, pos+speed, speed*2, track + "A"))  # greedy on straight line

            # reverse only when moving away from target in the next move
            if (speed > 0 and pos + speed > target) or (speed < 0 and pos + speed < target):
                lt.append((move + 1, pos, - abs(speed)/speed, track+"R"))

        return -1







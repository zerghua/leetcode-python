#
# Create by Hua on 8/4/22
#

"""
A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".


Example 1:

example-1
Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"



Constraints:

2 <= width, height <= 100
1 <= num <= 105
At most 104 calls in total will be made to step, getPos, and getDir.


robot will go around the perimeter, size == width * 2 + height*2 - 4
step = step % size
   W    W    W
 (0,2) (1,2) (2,2) (3,2)N
S(0,1)             (3,1)N
S(0,0) (1,0) (2,0) (3,0)
       E     E     E
width = 4, height = 3
if no steps,
    get_dir() should return EAST
else:
    getDir(return below)
    (1,0) (2,0) (3,0) should return EAST  [1 ~ width)[0]
    (3,1) (3,2) should return NORTH       [width-1][1 ~ height)
    (0,2) (1,2) (2,2) should return WEST  [0 ~ width)[height-1]
    (0,0) (0,1) should return SOUTH       [0][0 ~ height)

    getPos():
    step = step % size
    flatten perimeter into a list (need 100*100 cell) trade space for speed
    (0,0) .. (3,0) .. (3,2) .. (0,2), (0,1)
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    size = 10
    step = 1
    idx = 9

    if idx + step < size:
        idx = idx + step
    else:
        idx = step - (size - idx)

    08/04/2022 17:08	Accepted	539 ms	18.6 MB	python
    medium
    40 - 60 min.
    design
"""


class Robot(object):

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
           W    W    W
 (0,2) (1,2) (2,2) (3,2)N
S(0,1)             (3,1)N
S(0,0) (1,0) (2,0) (3,0)
       E     E     E
        """
        self.idx = 0
        self.moved = False
        self.width, self.height = width, height
        self.lt = []
        for i in range(width):
            self.lt.append((i, 0))

        for i in range(1, height):
            self.lt.append((width-1, i))

        for i in range(width - 2, -1, -1):
            self.lt.append((i, height - 1))

        for i in range(height - 2, 0, -1):
            self.lt.append((0, i))


    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.moved = True
        num = num % len(self.lt)
        if self.idx + num < len(self.lt):
            self.idx = self.idx + num
        else:
            self.idx = num - (len(self.lt) - self.idx)

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.lt[self.idx][0], self.lt[self.idx][1]]

    def getDir(self):
        """
        :rtype: str
        if no steps,
            get_dir() should return EAST
        else:
            getDir(return below)
            (1,0) (2,0) (3,0) should return EAST  [1 ~ width)[0]
            (3,1) (3,2) should return NORTH       [width-1][1 ~ height)
            (0,2) (1,2) (2,2) should return WEST  [0 ~ width)[height-1]
            (0,0) (0,1) should return SOUTH       [0][0 ~ height)

        """
        if not self.moved:  # corner case
            return "East"

        x,y = self.getPos()
        if 1<= x and 0 == y:
            return "East"
        if self.width-1 == x and 1 <= y:
            return "North"
        if 0 <= x and self.height-1 == y:
            return "West"
        if 0 == x and 0 <= y:
            return "South"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
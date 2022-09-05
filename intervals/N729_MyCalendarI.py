#
# Create by Hua on 9/5/22
#

"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.


## treemap solution
class MyCalendar {
    TreeMap<Integer, Integer> calendar;

    MyCalendar() {
        calendar = new TreeMap();
    }

    public boolean book(int start, int end) {
        Integer prev = calendar.floorKey(start),
                next = calendar.ceilingKey(start);
        if ((prev == null || calendar.get(prev) <= start) &&
                (next == null || end <= next)) {
            calendar.put(start, end);
            return true;
        }
        return false;
    }
}

from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx-1][1] > start) or (idx < len(self.calendar) and self.calendar[idx][0] < end):
            return False
        self.calendar.add((start, end))
        return True
"""


class Node():
    def __init__(self, s, e):
        self.start = s
        self.end = e
        self.left = None
        self.right = None

    def insert(self, s, e):
        if s >= self.end:
            if not self.right:
                self.right = Node(s, e)
                return True
            return self.right.insert(s, e)
        elif e <= self.start:
            if not self.left:
                self.left = Node(s, e)
                return True
            return self.left.insert(s,e)
        return False

class MyCalendar(object):

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        thought: segment tree(a kind of BST). store interval as value in the tree.
        https://leetcode.com/problems/my-calendar-i/discuss/109476/Binary-Search-Tree-python
        09/05/2022 14:54	Accepted	387 ms	14.5 MB	python
        further optimization is to provide a self-balancing function.
        the worst case here is o(n)
        medium - hard
        60-120min.
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)




import bisect
class MyCalendar_hack(object):

    def __init__(self):
        self.lt = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        thought:
        binary search hack.
        flatten the input into a list. a valid insertion will only be at even position
        [10,20, 30,35],  e.g input(25,28) their insert position should be the same and at even position
        then use bisect.

        https://leetcode.com/problems/my-calendar-i/discuss/760471/Python-Binary-Search-(better-than-95)-Logic-solution-Fully-explained

        09/05/2022 11:47	Accepted	487 ms	14.3 MB	python

        """
        left = bisect.bisect_left(self.lt, start)  # must use bisect_left to rule out cases of such [49,49] to [48,49]
        right = bisect.bisect_left(self.lt, end)   # must use end rather than end-1
        if left != right or left % 2 == 1:
            return False

        self.lt.insert(left, end-1)  # insert is o(n)?
        self.lt.insert(left, start)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



class MyCalendar_BF(object):

    def __init__(self):
        self.lt= []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool

        thought: since at most 1000 calls, then we can do BF, o(n^2) solution. each call check every pair
        if there is any intersection.
        use left and right edge to of the new to check if it's in the range of every previous pair.
        corner case: need to check both pairs edges.

        09/05/2022 11:17	Accepted	2166 ms	14.2 MB	python
        medium-easy if allowed BF o(n^2) solution.
        [3,7]
          [4, 8]

         [3,7]
       [1, 5]

          [3,7]
       [1,      9]

        """

        for left, right in self.lt:
            # simplier math is:
            # left < end and start < right:
            if left <= start <= right or left <= end-1 <= right or start <= left <= end-1 or start <= right <= end-1:
                return False

        self.lt.append([start, end-1])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
#
# Create by Hua on 9/21/22
#

"""
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).


Example 1:

Input
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
Output
[null, null, null, true, false, true]

Explanation
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is being tracked)
rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is still being tracked, despite the remove operation)


Constraints:

1 <= left < right <= 109
At most 104 calls will be made to addRange, queryRange, and removeRange.

thought:
this is more of a hack solution, binary search on an array. even index is open, odd index is close.
N715, calendarI used the same technique.

another method is to use segment tree or treemap.

In the example above of _X = [10, 15, 20, 25], lets say if we want to add a range [14, 22),
then at the end of the function, _X should look as follows [10, 25].

10,15,20,25
0  1  2  3
14=1
22=3
a[1:3] = []
# add
i = bl(a,10)=0
j = br(a,20)=0

10,20
0   1

# remove
i = bl(a,14)=1
j = br(a,16)=1
a[1:1]= [14]*(True) + [16]*(True)

e.g:
add [10,20], remove [14,16],  query [10,14] true, query [13,15] false, query [16, 17] true

[10,20]
[10,14,16,20]

bl(a,10)=0, i= br(a,10)=1
br(a,14)=2, j= bl(a,14)=1

i == j and i%2==1 return true

i = br(a,13) = 1
j = bl(a,15) = 2

i = br(a,16) = 3
i = br(a,17) = 3

# replace a closing item
add [10,20), add[15,25)
a= [10,20]
i = bl(a,15) = 1
j = br(a,25) = 2
a[1:2] = [25]
a= [10,25]


https://leetcode.com/problems/range-module/discuss/169353/Ultra-concise-Python-(only-6-lines-of-actual-code)-(also-236ms-beats-100)
https://leetcode.com/problems/range-module/discuss/244194/Python-solution-using-bisect_left-bisect_right-with-explanation

Time complexities are:

O(n) for addRange and removeRange, since slice overwriting dominates binary search
O(log n) for queryRange, since just binary search
where n is the number of disjoint intervals currently stored.

from bisect import bisect_left as bl, bisect_right as br

class RangeModule:

    def __init__(self):
        self._X = []

    def addRange(self, left, right):
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i%2 == 0) + [right]*(j%2 == 0)

    def queryRange(self, left, right):
        i, j = br(self._X, left), bl(self._X, right)
        return i == j and i%2 == 1

    def removeRange(self, left, right):
        i, j = bl(self._X, left), br(self._X, right)
        self._X[i:j] = [left]*(i%2 == 1) + [right]*(j%2 == 1)
Partial explanation:


k in [i, j) = [bl(X, left), br(X, right)) iff X[k] in [left, right]
k in [i, j) = [br(X, left), bl(X, right)) iff X[k] in (left, right)
Note that while x in [a, b) iff a <= x < b, for an interval [x, y) to be contained
within [a, b) we require a <= x < y <= b. In other words, both x and y are in [a, b].
This is how the transition from half-open to either open or closed occurs.


Typically problems like these require us to use a data structure like TreeMap (from Java) but for those of us using python, there is no such inbuilt data structure. And looking at this top solution in python, I was very confused as to how that works.

I'll try to explain how the algorithm works. The only thing we should understand clearly before understanding this solution is how bisect_left and bisect_right work in python. bisect_left gives the position of the first index where the element can be inserted and bisect_right gives the position of the last index where the element can be inserted. Note that if the item we are trying to search for is not present in the array, both bisect_left and bisect_right will return the same result.
eg : bl([1,2,3], 2) ==> 1 whereas br([1,2,3], 2) ==> 2
but for bl([1,2,4], 3) ==> 2 and br([1,2,4], 3) ==> 2

Now coming to the problem at hand, we internally represent the covered ranges by a single array _X. Think of this as a number line in which the even elements represent the beginning of a range and odd elements represent the end of the range. By definition of the range, we should maintain even number of elements in the array _X.

For e.g : _X = [10, 15, 20, 25] means the covered ranges are [10, 15) and [20, 25)

AddRange
If we want to add a range i.e addRange, we look at the bisect_left of left on the array and bisect_right of right on _X. We need to do this because the opening of the range (i.e left) has to preceed any other range which is closing at the same point. Similarly for the closing of the range i.e right, we have to keep in mind any other ranges opening at that point.

In the example above of _X = [10, 15, 20, 25], lets say if we want to add a range [14, 22), then at the end of the function, _X should look as follows [10, 25]..

For this to happen, we rely on i = bisect_left(...) and j=bisect_right(...).

What does it mean if i is odd ? If i is odd, that means that preceding element is an even element and the opening of the range is part of some other range. Similarly if j is odd, that also means if it is part of some other range and we need not create a new entry for it.

Next, what does it mean if i ie even ? This means that this point is not covered by any existing range and we have to create a new entry for it. Similar thing holds true for j (for j it would mean that we would have overwrite an exiting range).

The only other thing we have to pay attention to is to collapse all the other intermediate values of opening and closing points in the new interval. We accomplish this by collapsing the array self._X[i:j] = ...

RemoveRange
The intuition behind removeRange is similar to addRange, but the only difference is we have to perform the operation when i and j are odd instead of even. This is because while removing, if i is even, this means that it is not covered by any existing range and we need not perform any action (except possibly collapsing the ranges). Similar logic holds truee for j as well.

QueryRange
While querying for a range, we similarly get i and j values and we check for two conditions.

(i) Both i and j are same. i.e there is no range boundary in between left and right. if there is a range boundary, that means atleast some part of the range is not covered.
(ii) They should be odd. This means that a range has been opened by a preceeding even element and yet to be closed by the element at the i (or j)'th position.

If both (i) and (ii) are met, then we can say that the range is completely covered.

We do bisect_right(self._X, left) (and similarly bisect_left(self._X, right))because we want to be as conservative as we can.

For e.g if _X = [10,15], and we are querying for say [15, 20), then bisect_left(_X, left) would give us 1 . Which means that there is some part of the interval covered. but 15 is not covered in the range.

Time Complexity
We see that in addRange and removeRange, we are rewriting the array partially (can potentially rewrite the entire array). So their Time Complexity is O(n). For queryRange, the time complexity is O(logn) as the only thing we are doing is binary searches.

SpaceComplexity
O(n) for storing 2n points of the range.

09/21/2022 11:12	Accepted	795 ms	17.6 MB	python
hard
google.
binary search or segment tree(ordered tree so search is o(logn)).


similar problem:
352. Data Stream as Disjoint Intervals
2276. Count Integers in Intervals

segment tree solution. later
https://leetcode.com/problems/range-module/discuss/495876/Clean-And-Concise-Lazy-Propagation-Segment-Tree

"""



from bisect import bisect_left as bl, bisect_right as br
class RangeModule(object):

    def __init__(self):
        self.a = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        i,j = bl(self.a, left), br(self.a, right)
        self.a[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)  # add/replace if index is even

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        i,j = br(self.a, left), bl(self.a, right)  # search on the open brackets
        return i == j and i % 2 == 1   # fully cover only when i ==j and i is odd

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        i,j = bl(self.a, left), br(self.a, right)
        self.a[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)  # remove/replace if index is odd

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
#
# Create by Hua on 9/21/22
#

"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation:
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


Constraints:

1 <= length <= 5 * 104
0 <= index < length
0 <= val <= 109
0 <= snap_id < (the total number of times we call snap())
At most 5 * 104 calls will be made to set, snap, and get.


thought: create a list contains a list of lists(snap_id, value).
e.g:
0: [[0,0], [1,4], [5,2], [8,9]]
1: [[0,0], [10, 2]]
2: [[0,0]]

use 2 list to avoid TLE in python.
0: [0,1,5,8]    snap_list
0: [0,4,2,9]    val_list

# TLE cause
snap_list = [x[0] for x in self.a[index]]  # this is slow, will cause TLE


09/21/2022 16:23	Accepted	1020 ms	42 MB	python
medium
30min
google.
list of lists + binary search.
"""

import bisect


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.snap_list = []
        self.val_list = []
        for i in range(length):
            self.snap_list.append([0])
            self.val_list.append([0])

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """

        if self.snap_list[index][-1] == self.snap_id:  # check if match current snap_id
            self.val_list[index][-1] = val
        else:
            self.snap_list[index].append(self.snap_id)
            self.val_list[index].append(val)

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int

        can do binary search here. use bisect_right - 1
        """
        i = bisect.bisect_right(self.snap_list[index], snap_id) - 1
        return self.val_list[index][i]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
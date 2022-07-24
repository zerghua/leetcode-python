#
# Create by Hua on 7/24/22
#

"""
A Bitset is a data structure that compactly stores bits.

Implement the Bitset class:

Bitset(int size) Initializes the Bitset with size bits, all of which are 0.
void fix(int idx) Updates the value of the bit at the index idx to 1. If the value was already 1, no change occurs.
void unfix(int idx) Updates the value of the bit at the index idx to 0. If the value was already 0, no change occurs.
void flip() Flips the values of each bit in the Bitset. In other words, all bits with value 0 will now have value 1 and vice versa.
boolean all() Checks if the value of each bit in the Bitset is 1. Returns true if it satisfies the condition, false otherwise.
boolean one() Checks if there is at least one bit in the Bitset with value 1. Returns true if it satisfies the condition, false otherwise.
int count() Returns the total number of bits in the Bitset which have value 1.
String toString() Returns the current composition of the Bitset. Note that in the resultant string, the character at the ith index should coincide with the value at the ith bit of the Bitset.


Example 1:

Input
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
Output
[null, null, null, null, false, null, null, true, null, 2, "01010"]

Explanation
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // the value at idx = 3 is updated to 1, so bitset = "00010".
bs.fix(1);     // the value at idx = 1 is updated to 1, so bitset = "01010".
bs.flip();     // the value of each bit is flipped, so bitset = "10101".
bs.all();      // return False, as not all values of the bitset are 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "00101".
bs.flip();     // the value of each bit is flipped, so bitset = "11010".
bs.one();      // return True, as there is at least 1 index with value 1.
bs.unfix(0);   // the value at idx = 0 is updated to 0, so bitset = "01010".
bs.count();    // return 2, as there are 2 bits with value 1.
bs.toString(); // return "01010", which is the composition of bitset.


Constraints:

1 <= size <= 105
0 <= idx <= size - 1
At most 105 calls will be made in total to fix, unfix, flip, all, one, count, and toString.
At least one call will be made to all, one, count, or toString.
At most 5 calls will be made to toString.


thought: need to optimize below method(flip, all, one, count) to avoid TLE.
    At most 10^5 calls will be made in total to fix, unfix, flip, all, one, count, and toString.

how to optimize flip to be an o(1) operation? use extra storage for sure, but what?
just store flip times, also need to adjust other return method(will be tricky to code)

for fix and unfix, if flip % 2 == 0, it set normally,
else: reverse fix/unfix.

also for all/one/count/tostring, need to check flip parity.

in python the variable can't be the same as method name


07/24/2022 13:26	Accepted	1644 ms	48.2 MB	python
medium - hard
2h, stuck on optimize the perf and record ones correctly.



https://leetcode.com/problems/design-bitset/discuss/1748431/Python3-Java-C%2B%2B-All-Operations-O(1)-or-Flipped-StringFlip-Flag
class Bitset:
    def __init__(self, size: int):
        self.l = [0] * size
        self.ones = 0
        self.flipp = False

    def fix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 1: self.ones += 1
            self.l[idx] = 0
        else:
            if self.l[idx] == 0: self.ones += 1
            self.l[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.flipp:
            if self.l[idx] == 0: self.ones -= 1
            self.l[idx] = 1
        else:
            if self.l[idx] == 1: self.ones -= 1
            self.l[idx] = 0

    def flip(self) -> None:
        self.flipp = not self.flipp
        self.ones = len(self.l) - self.ones

    def all(self) -> bool: return self.ones == len(self.l)
    def one(self) -> bool: return self.ones > 0
    def count(self) -> int: return self.ones
    def toString(self) -> str:
        return ''.join([str(0 if i else 1) for i in self.l]) if self.flipp else ''.join([str(i) for i in self.l])

"""


class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.lt = [0] * size
        self.one_count = 0    # size of 1
        self.size = size  # total size
        self.flip_times = 0     # flip times


    def fix(self, idx):
        """
        record the actual ones.
        :type idx: int
        :rtype: None

        flip == 1, cur 0, actually it's 1, so after fix, it should be 1, count should not change
        flip == 1, cur 1, actually it's 0, so after fix, it should be 1, count should +=1

        flip == 2, cur 0, actually it's 0, so after fix, it should 1, count += 1
        flip == 2, cur 1, actually it's 1, so after fix, it should 1, count should not change

        """
        if self.flip_times % 2 == 0:  # normal case
            if self.lt[idx] == 0:
                self.one_count += 1
            self.lt[idx] = 1
        else:  # reverse case
            if self.lt[idx] == 1:
                self.one_count -= 1
            self.lt[idx] = 0

    def unfix(self, idx):
        """
        optimized
        :type idx: int
        :rtype: None
        """
        if self.flip_times % 2 == 0:  # normal case
            if self.lt[idx] == 1:
                self.one_count -= 1
            self.lt[idx] = 0
        else:  # reverse case
            if self.lt[idx] == 0:
                self.one_count += 1
            self.lt[idx] = 1

    def flip(self):
        """
        :rtype: None
        """
        self.flip_times += 1

    def all(self):
        """
        optimized
        :rtype: bool
        """
        return self.one_count == self.size if self.flip_times % 2 == 0 else self.one_count == 0

    def one(self):
        """
        optimized
        :rtype: bool
        """

        return self.one_count >= 1 if self.flip_times % 2 == 0 else self.one_count != self.size


    def count(self):
        """
        optimized
        :rtype: int
        """
        return self.one_count if self.flip_times % 2 == 0 else self.size - self.one_count


    def toString(self):
        """
        :rtype: str
        """
        if self.flip_times % 2 == 0:
            return "".join(str(i) for i in self.lt)
        else:
            return "".join(str(1-i) for i in self.lt)  # swap 0 and 1

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
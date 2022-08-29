#
# Create by Hua on 8/29/22
#

"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


Example 1:

Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"


Constraints:

1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

"""

import collections
import bisect
class TimeMap(object):

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None

        thought: 2 hashmaps + binary search, use hashmap with tuple will TLE since it's o(n) operation to get keys.
        08/29/2022 10:55	Accepted	894 ms	69.6 MB	python
        medium.
        """
        self.times[key].append(timestamp)
        self.values[key].append(value)


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str

        binary search, no duplicate timestamp and it's strictly increasing
        (1,x) (4,y) (8,z)
        """
        if key not in self.times:
            return ""

        #keys = [k[0] for k in lt]    # this will TLE since it's o(n) operation, let's separate timestamp and values into 2 lists
        idx = bisect.bisect(self.times[key], timestamp)
        return self.values[key][idx-1] if idx > 0 else ""





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
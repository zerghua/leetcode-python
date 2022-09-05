#
# Create by Hua on 8/29/22
#

"""
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.


Example 1:

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.


Constraints:

1 <= timestamp, price <= 109
At most 105 calls will be made in total to update, current, maximum, and minimum.
current, maximum, and minimum will be called only after update has been called at least once.
"""

import heapq
class StockPrice(object):

    def __init__(self):
        self.max_heap= []
        self.min_heap= []
        self.dt = {}
        self.latest = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None

        thought: we might not need hashmap since we are not interested in the history price,
        we just store max,min, and cur prices, and cur_timestamp, then we can answer the query

        trial and error: we need to store history data, since the future correct data will modify the
        min and max, so we need the second max and second min. we are also need to be aware which one
        gets modified, just store the second max/min is not enough.

        option 1: if we use list as data structure,  update will be o(n) since it needs to check every item
        in the list to make sure update the previous.
        max and min all also be o(n) since we need to check every item in the list.
        cur will be o(1), only check the last one.

        options 2: we need a treemap(red-blac tree) like data structure, which is a hashmap, but also store the
        sorted price, each update will be o(logn), max/min be o(logn), cur be o(1)

        corner case: the max or min value can be corrected, so we need to adjust it.

        option 3: use 2 heaps to store max and min, a hashmap to store (ts, price), and it's accurate always.
        check each price at the top of heap matches the record in hashmap, if not, means it's been updated, that data
        is obsolete, we can remove it.
        
        09/05/2022 10:37	Accepted	1750 ms	62.8 MB	python
        60min. 
        medium - hard if using python, since python does not have treemap. used 2 heaps + hashmap
        medium for java.

        """
        self.latest = max(self.latest, timestamp)
        self.dt[timestamp] = price
        heapq.heappush(self.max_heap, (-1 * price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self):
        """
        :rtype: int
        """
        return self.dt[self.latest]

    def maximum(self):
        """
        :rtype: int
        """
        while -1*self.max_heap[0][0] != self.dt[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)

        return -1*self.max_heap[0][0]


    def minimum(self):
        """
        :rtype: int

            remove the top of the heap, if the (ts: price) not in hashmap record.
        """
        while self.min_heap[0][0] != self.dt[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)

        return self.min_heap[0][0]

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
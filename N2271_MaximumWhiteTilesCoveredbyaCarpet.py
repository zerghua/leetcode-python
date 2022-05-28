#
# Create by Hua on 5/26/22
#


"""
You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.



Example 1:


Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10.
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:


Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10.
It covers 2 white tiles, so we return 2.


Constraints:

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
The tiles are non-overlapping.

"""


class Solution(object):
    def maximumWhiteTiles(self, tiles, carpetLen):
        """
        :type tiles: List[List[int]]
        :type carpetLen: int
        :rtype: int

        thought:
        2 pointers and sliding window.

        j  j  j  j
        0  1  2  3
        WW WW WW WWWWWWW
        CCCCCCCCCCC


        WW WW WW WWWWWWW
           CCCCCCCCCCC
           i(1)

        WW WW WW WWWWWWW
              CCCCCCCCCCC
              i(2)

        WW WW WW WWWWWWW
                 CCCCCCCCCCC
                 i(3)

        wwww  (1,2)(3,4)
        c

        05/26/2022 16:48	Accepted	1616 ms	38.8 MB	python
        medium - hard 30-60 min. easy to think of sliding window, but very hard to come up with the
        correct code.

        more thought on the next day:
        while (ret < carpetLen), when carpet smaller than any one of the
        tiles, we stop, the result will just be len(carpet).
        each time we move to the start of next tile, calculate the complete
        cover and partial cover, do an update. release previous tile.
        """
        tiles.sort(key=lambda x : x[0])
        left = right = cover = ret = 0
        n = len(tiles)
        while right < n and ret < carpetLen:
            if tiles[left][0] + carpetLen > tiles[right][1]:
                cover += tiles[right][1] - tiles[right][0] + 1
                ret = max(ret, cover)
                right += 1
            else:
                partial = max(0, tiles[left][0] + carpetLen - tiles[right][0])
                ret = max(ret, cover + partial)
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1

        return ret




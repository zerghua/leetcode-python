#
# Create by Hua on 4/1/22.
#

"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

    "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
    "./" : Remain in the same folder.
    "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.



Example 1:

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

Example 2:

Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0



Constraints:

    1 <= logs.length <= 103
    2 <= logs[i].length <= 10
    logs[i] contains lowercase English letters, digits, '.', and '/'.
    logs[i] follows the format described in the statement.
    Folder names consist of lowercase English letters and digits.


"""


class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int

        thought: maintain how deep did we go.
        corner case: deep should never go negative.
        04/01/2022 16:02	Accepted	16 ms	13.7 MB	python
        easy 5 min.
        """

        deep = 0
        for s in logs:
            if s[0] == '.':
                if s[1] == '.':
                    deep -= 1
                    deep = max(0, deep)
            else:
                deep += 1

        return deep

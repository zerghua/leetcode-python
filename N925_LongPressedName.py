#
# Create by Hua on 5/11/22
#


"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.


Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.

"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool

        thought: string comparison, 2 pointers
        05/11/2022 10:18	Accepted	30 ms	13.4 MB	python
        easy - medium. 10-20 min. corner cases.
        """

        if len(name) > len(typed): return False
        i = j = 0
        last = ""
        m,n = len(name), len(typed)
        while i < m and j < n:
            if name[i] == typed[j]:
                last = name[i]
                i += 1
                j += 1
            else:  # char not equal
                if typed[j] != last:
                    return False
                else:  # equal last char, skip long pressed
                    while j<n and typed[j] == last:
                        j += 1
        while j < n and typed[j] == last:  # corner case, "vtkgn", "vttkgnn", return True
            j += 1
        return i == m and j == n
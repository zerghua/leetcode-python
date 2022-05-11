#
# Create by Hua on 5/11/22
#


"""
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

"""


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str

        thought: two pointers. reverse only letters
        05/11/2022 14:25	Accepted	35 ms	13.5 MB	python
        easy. 5-10 min. two pointers
        """

        n = len(s)
        i,j = 0,n-1
        a = list(s)
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:  # now both i and j are letters, switch them
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        return str(a)
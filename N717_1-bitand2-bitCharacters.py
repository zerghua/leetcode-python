#
# Create by Hua on 5/17/22
#


"""
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.



Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.


Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.

"""


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool

        thought:
        1110    false
        1100    true
        1111  ->invalid

        1010    false
        1000    true
        1011 -> invalid

        0010    false
        0110    true
        0000    true
        0100    true

        100     true
        110     true
        010     false
        011     false

        so from left to right, if encounter 1, it's next must be 0 or 1, then we can i+2, else encounter 0, i+1
        so, we loop stop @n-2, then if i == n-1 then it's true, else false

        05/17/2022 13:13	Accepted	52 ms	13.4 MB	python
        easy-medium 10-20 min.
        """
        i, n = 0, len(bits)
        while i< n-1:
            if bits[i] == 1:
                i+=2
            else:
                i+=1
        return i == n-1

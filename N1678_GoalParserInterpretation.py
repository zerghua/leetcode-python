#
# Create by Hua on 3/27/22.
#

"""
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.



Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"



Constraints:

    1 <= command.length <= 100
    command consists of "G", "()", and/or "(al)" in some order.


"""


class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str

        thought: simple string check.
        command consists of "G", "()", and/or "(al)" in some order.
        03/27/2022 11:32	Accepted	20 ms	13.3 MB	python
        5 min. easy. string check.
        """
        n = len(command)
        ret = list()
        i = 0
        while i < n:
            if command[i] == "G":
                ret.append("G")
                i += 1
            elif command[i] == "(" and command[i+1] == ")":
                ret.append("o")
                i +=2
            else:
                ret.append("al")
                i +=4
        return "".join(ret)




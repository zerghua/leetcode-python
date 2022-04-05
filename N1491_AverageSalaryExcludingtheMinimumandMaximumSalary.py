#
# Create by Hua on 4/5/22.
#

"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.



Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000



Constraints:

    3 <= salary.length <= 100
    1000 <= salary[i] <= 106
    All the integers of salary are unique.


"""


class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float

        thought: get avg without max and min, return float
        04/05/2022 09:58	Accepted	45 ms	13.3 MB	python
        easy 1min. sort. might not even need to sort. get max and min then
        do substraction
        """

        n = len(salary)
        s = sorted(salary)
        return (float)(sum(s[1:-1])) / (n-2)

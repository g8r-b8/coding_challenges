#Dec 9; 2:03PM

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        reversed_int = int(str(x)[::-1])
        return (reversed_int == x)

"""

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Example 2:

"int_palindrom_LC.py" 42L, 778B


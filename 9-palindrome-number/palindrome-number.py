class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = [d for d in str(x)]
        return n == n[::-1]
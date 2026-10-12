class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(ch for ch in s if ch.isalnum()).lower().strip()

        for i in range(len(a)):

            if a[i] != a[-1-i]:
                return False
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(ch for ch in s if ch.isalnum()).lower()
        for i in range(len(a)//2):
            if a[i] != a[-1-i]:
                return False
        return True
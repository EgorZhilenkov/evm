# решение которое я сдал

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]


# или если все-таки через 2 указателя
class Solution:
    def isPalindrome(self, s: str) -> bool:

        import re

        s = re.sub("[^a-zA-Z0-9]", "", s).lower()

        start = 0
        end = len(s) - 1

        while start <= end:

            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True
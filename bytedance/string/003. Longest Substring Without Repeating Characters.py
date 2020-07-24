# Time Complexity: O(N)
# Python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        o = set()
        ans, r = 0, -1
        n = len(s)
        for i in range(n):
            if i != 0: 
                o.remove(s[i - 1])
            while r + 1 < n and s[r + 1] not in o:
                o.add(s[r + 1])
                r += 1
            ans = max(ans, r - i + 1)
        return ans


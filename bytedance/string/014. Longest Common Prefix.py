# Solution 1 compare every character vertically in **two row**
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = [len(set(c)) == 1 for c in zip(*strs)] + [0]
        return str[0][:r.index(0)] if strs else ''


# Solution 2 compare every character vertically
class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        for i in zip(*str):
            tmp_set = set(i)
            if len(tmp_set) == 1:
                res += i[0]
            else:
                break
        return res

# Solution 3 compare one by one
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not strs: return ''
        a = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(a) != 0:
                a = a[:len(a)-1]
        return a
# or
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not s: return ''

        prefix, count = s[0], len(s)
        for i in range(1, count):
            prefix = self.lcp(prefix, s[i])
            if not prefix:
                break
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

# Solution 4 compare the first and last one after sorting.
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        a, b, res = s[0], s[-1], ''
        for i in range(len(a)):
            if a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
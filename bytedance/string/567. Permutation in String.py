class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Explanation in Chinese: https://leetcode-cn.com/problems/permutation-in-string/solution/zheng-li-de-zui-quan-jie-ti-si-lu-by-aijdf/

        l1 = len(s1)
        l2 = len(s2)
        l = r = cnt = 0
        c1 = collections.Counter(s1)
        c2 = collections.Counter()
        while r < l2:
            c2[s2[r]] += 1
            if c1[s2[r]] == c2[s2[r]]:
                cnt += 1
            if cnt == len(c1):
                return True
            r += 1
            if r - l + 1 > l1:
                if c1[s2[l]] == c2[s2[l]]:
                    cnt -= 1
                c2[s2[l]] -= 1
                if c2[s2[l]] == 0:
                    del c2[s2[l]]
                l += 1
        return False

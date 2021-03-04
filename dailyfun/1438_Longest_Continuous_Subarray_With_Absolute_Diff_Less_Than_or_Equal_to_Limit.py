from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums: return 0
        windows = SortedList()
        l = r = res = 0
        n = len(nums)
        while r < n:
            windows.add(nums[r])
            while windows[-1] - windows[0] > limit:
                windows.remove(nums[l])
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
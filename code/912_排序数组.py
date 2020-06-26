# https://leetcode-cn.com/problems/sort-an-array/

# Bubble sort. Over time.
# i and j should both start from 0
# Time Complexity  - O(n²)
# Space complexity - O(1)
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            s = False
            for j in range(0, len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    s = True
            if not s: break
        return nums

# Insertion sort. Over time.
# Time Complexity  - O(n²)
# Space complexity - O(1)
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            value = nums[i]
            j = i - 1
            while j >= 0:
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j -= 1
                else:
                    break
            nums[j+1] = value
        return nums

# Selection sort. Over time.
# Time Complexity  - O(n²)
# Space complexity - O(1)
class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            m = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[m]:
                    m = j
            if m != i:
                nums[i], nums[m] = nums[m], nums[i]
        return nums
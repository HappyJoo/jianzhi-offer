# DP 动态规划
# golang
```
func lengthOfLIS(nums []int) int {
    res := 1

    dp := make([]int, len(nums))
    for i:=0; i < len(nums); i++ {
        dp[i] = 1
        for j := 0; j < i; j++ {
            if nums[j] < nums[i] {
                dp[i] = max(dp[i], dp[j] + 1)
                res = max(res,dp[i])
            }
        }
    }
    return res
}

func max(x,y int) int {
    if x > y {
        return x
    }
    return y
}
```
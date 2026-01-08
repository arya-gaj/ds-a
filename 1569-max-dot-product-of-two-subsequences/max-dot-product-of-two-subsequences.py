class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                take = nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1])
                skip1 = dp[i + 1][j]
                skip2 = dp[i][j + 1]
                dp[i][j] = max(take, skip1, skip2)
        
        return dp[0][0]        
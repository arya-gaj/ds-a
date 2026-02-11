class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = 0
        max_reachable = 0
        curr_reachable = 0
        n = len(nums)

        if n <= 1:
            return 0

        for i in range(0, n - 1):
            curr_reachable = max(curr_reachable, i + nums[i])

            if i == max_reachable:
                max_reachable = curr_reachable
                jumps += 1

        return jumps
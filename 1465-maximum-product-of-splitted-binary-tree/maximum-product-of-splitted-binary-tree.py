class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_product = 0

        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            sub_sum = node.val + left_sum + right_sum

            self.max_product = max(
                self.max_product,
                sub_sum * (total - sub_sum)
            )

            return sub_sum

        dfs(root)

        return self.max_product % MOD        
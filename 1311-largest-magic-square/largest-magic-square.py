class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def get_row(i, j, k):
            return row[i][j + k] - row[i][j]

        def get_col(i, j, k):
            return col[i + k][j] - col[i][j]

        def get_diag1(i, j, k):
            return diag1[i + k][j + k] - diag1[i][j]

        def get_diag2(i, j, k):
            return diag2[i + k][j] - diag2[i][j + k]

        ans = 1
        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    target = get_row(i, j, k)
                    ok = True

                    if get_diag1(i, j, k) != target or get_diag2(i, j, k) != target:
                        continue

                    for t in range(k):
                        if get_row(i + t, j, k) != target or get_col(i, j + t, k) != target:
                            ok = False
                            break

                    if ok:
                        ans = k
        return ans        
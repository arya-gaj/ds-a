class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans = []
        self.combine(candidates, target, 0, [], 0)
        return self.ans

    def combine(self, candidates: List[int], target: int, curr: int, selected: List[int], index: int) -> None:
        if curr == target:
            self.ans.append(selected.copy())
            return

        if curr > target:
            return

        prev = -1
        for i in range(index, len(candidates)):
            # skip duplicates at the same recursion depth
            if candidates[i] == prev:
                continue

            selected.append(candidates[i])
            self.combine(candidates, target, curr + candidates[i], selected, i + 1)
            selected.pop()

            prev = candidates[i]
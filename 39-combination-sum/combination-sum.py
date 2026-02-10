class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans=[]
        self.combine(candidates, [], 0, target, 0)
        return self.ans

    def combine(self, candidates: List[int], res:List[int], curr: int, target: int, index: int ) -> None:
        if curr==target:
            self.ans.append(res.copy())
            return
        if curr>target or index==len(candidates):
            return
        
        res.append(candidates[index])
        curr+=candidates[index]
        self.combine(candidates, res, curr, target, index)
        res.pop()
        curr-=candidates[index]
        self.combine(candidates, res, curr, target, index+1)

        return
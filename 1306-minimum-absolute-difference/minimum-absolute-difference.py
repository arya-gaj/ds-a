class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        m = min(map(sub,a:=sorted(a)[::-1],a[1:]))
        return [[v,u] for v,u in pairwise(a[::-1]) if u-v==m]
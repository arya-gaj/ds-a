class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10**18
        strs = set(original) | set(changed)
        mp = {s:i for i,s in enumerate(strs)}
        m = len(mp)
        dist = [[INF]*m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
        for o,c,w in zip(original, changed, cost):
            u,v = mp[o], mp[c]
            dist[u][v] = min(dist[u][v], w)
        for k in range(m):
            for i in range(m):
                if dist[i][k] == INF: 
                    continue
                for j in range(m):
                    if dist[k][j] < INF and dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        from collections import defaultdict
        by_len = defaultdict(list)
        for s in mp:
            by_len[len(s)].append(s)

        n = len(source)
        dp = [INF]*(n+1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == INF:
                continue
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            for L, arr in by_len.items():
                if i+L > n:
                    continue
                s1 = source[i:i+L]
                s2 = target[i:i+L]
                if s1 in mp and s2 in mp:
                    u,v = mp[s1], mp[s2]
                    if dist[u][v] < INF:
                        dp[i+L] = min(dp[i+L], dp[i] + dist[u][v])

        return -1 if dp[n] == INF else dp[n]        
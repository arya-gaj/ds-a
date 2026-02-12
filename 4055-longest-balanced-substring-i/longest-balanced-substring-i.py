class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        s = [ord(char) - ord('a') for char in s]

        result = 0
        for l in range(n):
            if n - l <= result:
                break

            cnt = [0] * 26
            uniq = maxfreq = 0
            for r in range(l, n):
                i = s[r]

                uniq += cnt[i] == 0
                cnt[i] += 1
                if cnt[i] > maxfreq:
                    maxfreq = cnt[i]

                cur = r - l + 1
                if uniq * maxfreq == cur and cur > result:
                    result = cur

        return result
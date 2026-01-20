from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []

        w = len(words[0])
        n = len(words)
        need = Counter(words)
        res = []

        for start in range(w):
            left = start
            seen = Counter()
            count = 0

            for right in range(start, len(s) - w + 1, w):
                word = s[right: right+w]

                if word not in need: # variables reset logic
                    seen.clear()
                    count = 0
                    left = right + w
                    continue

                seen[word] += 1
                count += 1

                while seen[word] > need[word]:
                    left_word = s[left: left+w]
                    seen[left_word] -= 1
                    count -= 1
                    left += w

                if count == n:
                    res.append(left)

        return res
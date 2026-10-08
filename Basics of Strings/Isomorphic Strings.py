class Solution:
    def isomorphicString(self, s: str, t: str) -> bool:
        freq = {}
        reverse = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in freq and freq[a] != b:
                return False

            if b in reverse and reverse[b] != a:
                return False

            freq[a] = b
            reverse[b] = a
            

            
        return True
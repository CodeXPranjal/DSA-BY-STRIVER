class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False

        for i in s:
            if s==goal:
                return True
            else:
                s = s[1:]+s[0]
        return s == goal
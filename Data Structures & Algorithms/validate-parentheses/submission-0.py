class Solution:
    def isValid(self, s: str) -> bool:
        dp = { "]": "[", ")":"(","}":"{"}
        stack = []

        for c in s:
            if c not in dp:
                stack.append(c)
            else:
                if stack and stack[-1] == dp[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0 
            
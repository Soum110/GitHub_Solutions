class Solution:
    def isValid(self, s: str) -> bool:
        stk = [s[0]]
        for i in range(1, len(s)):
            if stk and ((stk[-1] == '(' and s[i] == ')') or (stk[-1] == '{' and s[i] == '}') or (stk[-1] == '[' and s[i] == ']')):
                stk.pop()
            else:
                stk.append(s[i])
        
        if not stk:
            return True
        else:
            return False

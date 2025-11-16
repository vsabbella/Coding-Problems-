class Solution(object):
    def isValid(self,s):
        parenthesis = {
                        '(':')',
                        '{':'}',
                        '[':']'
                       }
        inv_parenthesis ={v:k for k,v in parenthesis.items()}
        
        stack = []
        for c in s:
            if c in parenthesis:
                stack.append(c)
            elif c in inv_parenthesis:
                if len(stack) == 0 or stack[-1] != inv_parenthesis[c]:
                    return False
                else:
                    stack.pop()
    
        return len(stack)==0
    

print(Solution().isValid('(){([])}'))
#True    
print(Solution().isValid('(){(['))
#False    
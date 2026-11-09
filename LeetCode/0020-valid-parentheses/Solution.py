class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Input: s = "()[]{}"
        '''
        hashmap = {")":"(","]":"[","}":"{"}
        stack = []
        for c in s:
            if c in hashmap and stack:
                c2 = stack.pop()
                if hashmap[c] != c2:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
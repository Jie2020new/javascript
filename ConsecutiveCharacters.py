class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        @author: Jie
        """
        
        sLen = len(s)
        if sLen <= 1: return sLen
        
        longest = 1
        subLongest = 1
        while (sLen > 1):
            sLen-=1
            if s[sLen] == s[sLen-1]:
                subLongest +=1
                if sLen == 1:
                    longest = max(subLongest, longest)
            else:
                longest = max(subLongest, longest)
                subLongest =1
                
            
        return longest
                
            

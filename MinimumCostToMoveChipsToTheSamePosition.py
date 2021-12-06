# @author Jie
#
#***

class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        positionLen = len(position)
        
        if positionLen <= 1: return 0
        
        totalOdd = 0
        totalEven = 0
        for pos in position:
            if pos%2 == 0:
                totalOdd += 1
            else:
                totalEven += 1
        
        return  totalEven if (totalOdd)>(totalEven) else (totalOdd)

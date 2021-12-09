class Solution(object):
    def canReach(self, arr, start):
        """
        :@author: Jie
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        arrLen = len(arr)
        if (start > (len(arr)-1) or start <0): return False
        if (arrLen > 50000 or arrLen <1): return False
        
        
        if (0 in arr):
            if (sum(arr) == (arrLen-1)): return True
            layer = []
            leftNode = start - arr[start]
            rightNode = start + arr[start]
        
            if (leftNode)>=0 and (leftNode<arrLen):
                if arr[leftNode] == 0: return True
                if leftNode in layer: pass
                else: layer.append(leftNode)
                
            if (rightNode)>=0 and (rightNode<arrLen):
                if arr[rightNode] == 0: return True
                if rightNode in layer: pass
                else:layer.append(rightNode)
              
            layerNodeNum = len(layer)    
            
            maxSteps = max(start, arrLen-start)
            while(layerNodeNum>0 and maxSteps>-1):
                maxSteps-=1
                nextLayer = []
            
                for x in layer:
                    leftNode = x - arr[x]
                    rightNode = x + arr[x]
                    if (leftNode)>=0 and (leftNode<arrLen):
                        if arr[leftNode] == 0: return True
                        if leftNode in nextLayer: pass
                        else: nextLayer.append(leftNode)
                    if rightNode>=0 and rightNode<arrLen:
                        if arr[rightNode] == 0: return True
                        if rightNode in nextLayer: pass
                        else:nextLayer.append(rightNode)
                    
                layer = nextLayer
                layerNodeNum = len(layer)
        
        return False
            

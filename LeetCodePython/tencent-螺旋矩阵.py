from math import ceil
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return []
        height=len(matrix)
        width=len(matrix[0])
        x=0
        y=0
        num=ceil(min(height,width)/2)
        res=[]
        for i in range(0,num):
            if i!=0:
                res.append(matrix[x][y])
                y+=1
            for j in range(0,width-1):
                res.append(matrix[x][y])
                y+=1
            for j in range(0,height-1):
                res.append(matrix[x][y])
                x+=1
            if height-1>0:
                for j in range(0,width-1):
                    res.append(matrix[x][y])
                    y-=1
            else:
                res.append(matrix[x][y])
            if width-1>0:
                for j in range(0,height-2):
                    res.append(matrix[x][y])
                    x-=1
            elif height-1>0:
                res.append(matrix[x][y])
            height-=2
            width-=2
        if res[-1]!=matrix[x][y]:
            res.append(matrix[x][y])
        return res
        
t=Solution()
print(t.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
print(t.spiralOrder([[6,9,7]]))
print(t.spiralOrder([[1,2],[3,4]]))
# 82.61

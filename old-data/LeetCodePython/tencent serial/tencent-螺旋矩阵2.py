from math import ceil
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        height=n
        width=n
        x=0
        y=0
        num=ceil(width/2)
        t=1
        res=[]
        for i in range(n):
            res.append([])
            for j in range(n):
                res[i].append(0)
        for i in range(0,num):
            if i!=0:
                res[x][y]=t
                t+=1
                y+=1
            for j in range(0,width-1):
                res[x][y]=t
                t+=1
                y+=1
            for j in range(0,height-1):
                res[x][y]=t
                t+=1
                x+=1
            if height-1>0:
                for j in range(0,width-1):
                    res[x][y]=t
                    t+=1
                    y-=1
            else:
                res[x][y]=t
                t+=1
            if width-1>0:
                for j in range(0,height-2):
                    res[x][y]=t
                    t+=1
                    x-=1
            elif height-1>0:
                res[x][y]=t
                t+=1
            height-=2
            width-=2
        if res[x][y]==0:
            res[x][y]=t
        return res

t=Solution()
print(t.generateMatrix(5))
# 94.93

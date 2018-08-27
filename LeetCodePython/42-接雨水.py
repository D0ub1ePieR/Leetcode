class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height=[0]+height
        height.append(0)
        l=len(height)
        mid=[]
        res=0
        for i in range(1,l-1):
            if height[i-1]<=height[i] and height[i]>height[i+1]:
                mid.append(i)
        if mid==[]:
            return 0
        mid=[0]+mid+[0]
        while 1:
            num=0
            tmid=[]
            for i in range(1,len(mid)-1):
                if height[mid[i-1]]<=height[mid[i]] and height[mid[i]]>height[mid[i+1]]:
                    tmid.append(i)
                    num+=1
            if num==1:
                break
            #print(mid,tmid,"---")
            t=mid[:tmid[0]]+mid[tmid[-1]+1:]
            for i in tmid:
                t.append(mid[i])
            t.sort()
            t=t[1:]+[0]
            mid=t
            #print(mid,tmid,"===")
        mid=mid[1:-1]
        lm=len(mid)
        for i in range(lm-1):
            tmp=min(height[mid[i]],height[mid[i+1]])
            for j in range(mid[i],mid[i+1]):
                if tmp>height[j]:
                    res=res+tmp-height[j]
                    #print(tmp-height[j])
        return res

t=Solution()
print(t.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
print(t.trap([1,0,2,1,0,1,3,2,1,2,1]))

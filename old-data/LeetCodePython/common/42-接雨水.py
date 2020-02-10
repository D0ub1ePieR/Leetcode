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
                if height[mid[i-1]]<=height[mid[i]] and height[mid[i]]>=height[mid[i+1]]:
                    if i+2<len(mid) and height[mid[i]]==height[mid[i+1]] and height[mid[i+1]]<height[mid[i+2]]:
                        continue
                    tmid.append(i)
                    if height[mid[i]]!=height[mid[i+1]]:
                        num+=1
            if num==1:
                break
            #print(mid,tmid,"---")
            t=mid[:tmid[0]]+mid[tmid[-1]:]
            for i in range(len(tmid)-1):
                t.append(mid[tmid[i]])
                mm=min(height[mid[tmid[i]]],height[mid[tmid[i+1]]])
                for j in range(tmid[i]+1,tmid[i+1]):
                    if height[mid[j]]>mm:
                        t.append(mid[j])
            t.sort()
            t=t[1:]+[0]
            mid=t
            #print(mid,tmid,"===")
        mid=mid[1:-1]
        #print("mid",mid)
        lm=len(mid)
        for i in range(lm-1):
            tmp=min(height[mid[i]],height[mid[i+1]])
            for j in range(mid[i],mid[i+1]):
                if tmp>height[j]:
                    res=res+tmp-height[j]
                    #print(tmp,height[j])
        return res

t=Solution()
print(t.trap([6,7,6,3,5,7,1,4,2,0,5,8,2,9,5,1,3,1,0]))
print(t.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
print(t.trap([1,4,3,4,0,0,2,6,0,8,9,4,5,6,5,2,6,7]))

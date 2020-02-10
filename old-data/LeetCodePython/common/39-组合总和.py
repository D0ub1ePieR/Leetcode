class Solution:
    def figure(self, reslist, numlist, num, res):
        if numlist==[]:
            return
        for i in numlist:
            tmp=1
            while num-i*tmp>0:
                t=reslist[:]
                t.extend([i]*tmp)
                self.figure(t,numlist[numlist.index(i)+1:],num-i*tmp, res)
                tmp+=1
            if num-i*tmp==0:
                t=reslist[:]
                t.extend([i]*tmp)
                t.sort()
                res.append(t)
    def combinationSum(self, candidates, target):
        res=[]
        candidates.sort()
        candidates.reverse()
        self.figure([],candidates,target, res)
        return res

t=Solution()
print(t.combinationSum([2,3,6,7],7))
print(t.combinationSum([2,3,5],8))

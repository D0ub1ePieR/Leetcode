class Solution:
    def figure(self, reslist, numlist, num, res):
        if numlist==[]:
            return
        for i in numlist:
            if num-i>0:
                t=reslist[:]
                t.extend([i])
                self.figure(t,numlist[numlist.index(i)+1:],num-i, res)
            if num-i==0:
                t=reslist[:]
                t.extend([i])
                t.sort()
                res.append(t)
    def combinationSum2(self, candidates, target):
        res=[]
        candidates.sort()
        candidates.reverse()
        self.figure([],candidates,target, res)
        return res

t=Solution()
print(t.combinationSum([2,3,6,7],7))
print(t.combinationSum([2,3,5],8))
print(t.combinationSum([10,1,2,7,6,1,5],8))

class solution:
    def countAndSay(self,n):
        l=['1']
        for i in range(n-1):
            pre=l[0]
            count=0
            t=[]
            for j in l:
                if j!=pre:
                    t.extend([str(count),pre])
                    count=1
                    pre=j
                else:
                    count+=1
            t.extend([str(count),pre])
            l=t
        return ''.join(l)

a=solution()
for i in range(1,10):
    print(a.countAndSay(i))

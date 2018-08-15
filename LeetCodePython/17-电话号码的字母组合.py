class solution:
    def letterCombinations(self,digits):
        pd={'2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            }
        num=list(digits)
        if num==[]:
            return []
        res=['']
        for c in num:
            tmp=[]
            for r in res:
                for t in pd[c]:
                    tmp.append(r+t)
            res=tmp
        return res
    
t=solution()
print(t.letterCombinations(''))

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res=""
        status=1
        for ch in str:
            if status==1:
                if ch.isdigit():
                    res+=ch
                    status=2
                elif ch in ['-','+']:
                    status=3
                    res+=ch
                elif ch==" ":
                    status=5
            elif status==2:
                if ch.isdigit():
                    res+=ch
                else:
                    status=4
            elif status==3:
                if ch.isdigit():
                    res+=ch
                    status=2
                else:
                    return 0
            elif status==4:
                if int(res) in range(-pow(2,31),pow(2,31)):
                    return int(res)
                elif int(res)<0:
                    return -pow(2,31)
                else:
                    return pow(2,31)-1
            elif status==5:
                if ch.isdigit():
                    res+=ch
                    status=2
                elif ch in ['-','+']:
                    res+=ch
                    status=3
                elif ch!=' ':
                    return 0
        if res=="" or res=="-" or res=="+":
            return 0
        else:
            if int(res) in range(-pow(2,31),pow(2,31)):
                return int(res)
            elif int(res)<0:
                return -pow(2,31)
            else:
                return pow(2,31)-1

test=Solution()
print(test.myAtoi("    010"))

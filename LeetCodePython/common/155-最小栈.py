import heapq
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__size=0
        self.__stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.__size+=1
        self.__stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.__size-=1
        del self.__stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.__stack[self.__size-1]

    def getMin(self):
        """
        :rtype: int
        """
        return heapq.nsmallest(1,self.__stack)[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 17.62

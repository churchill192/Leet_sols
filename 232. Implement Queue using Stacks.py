class MyQueue:

    def __init__(self):
        self.list1=[]
        

    def push(self, x: int) -> None:
        self.list1.append(x)
        

    def pop(self) -> int:
        return self.list1.pop(0)


    def peek(self) -> int:
        return self.list1[0]

    def empty(self) -> bool:
        if len(self.list1)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
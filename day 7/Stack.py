class Stack :
    def __init__(self):
        self.stack=[]
        self.size=0
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    def pop(self):
        if(self.size==0):
            return None
        else :
         self.size-=1
    def peek(self):
        if(self.size==0):
            return None
        else :
            return self.stack[self.size-1]
    def isEmpty(self):
        if(self.size==0):
            return True
        else :
            return False
    def Size(self):
        return self.size
        

s1=Stack()
s1.push(9)
s1.push(11)
s1.push(23)
print(s1.peek())
s1.pop()
print(s1.peek())
print(s1.isEmpty())
print(s1.Size())
        
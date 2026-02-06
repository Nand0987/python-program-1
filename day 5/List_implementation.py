class MyList:
    def __init__(self):
        self.capacity=4
        self.size=0
        self.data=[None]*self.capacity
    def _resize(self):
        self.capacity=self.capacity*2
        new_data=[None]*self.capacity
        for i in range(self.capacity/2):
         self.new_data[i]=data[i]
        self.data=new_data

    def append(self,value):
        if(self.size==self.capacity):
            self._resize()
        self.data[self.size]=value
        self.size+=1
    def display(self):
        for i in range(self.size):
            print(self.data[i])
    def remove(self,value):
        for i in range(self.size):
            if self.data[i]==value:
                break
        for i in range(i,self.size-1):
            self.data[i]=self.data[i+1]
        self.size-=1


l1=MyList()
l1.append(4)
l1.append(9)
l1.append(3)
l1.append(7)
# l1.display()
l1.remove(9)
l1.display()



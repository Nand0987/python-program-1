class Queue :
    def __init__(self,capacity):
        self.capacity=capacity
        self.queue=[None]*capacity
        self.front=-1
        self.rear=-1
    def is_empty(self):
        return self.front==-1
    def is_Full(self):
        return self.rear==self.capacity-1 
    def enqueue(self,data):
        if self.is_Full():
            print("queue is full")
        if self.front==-1 :
            self.front=0
        self.rear+=1
        self.queue[self.rear]=data
        print("data inserted successfully")
    def peek(self):
        
            
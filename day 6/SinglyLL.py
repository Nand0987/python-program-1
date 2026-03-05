class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLL:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        self.next=self.head
        self.head=new_node
    # def display(self):
    #     self.temp=self.next
    #     while temp :
    #         print(temp.data)
    #         temp=temp.next
l1=SinglyLL()
l2=SinglyLL()
l1.insert_at_begin(23)
l1.insert_at_begin(34)




from dsa.node import MyNode

class MyLinkedList:
    def __init__(self):
        self.__size = 0
        self.__head = MyNode()


    def getSize(self):
        return self.__size

    def insert(self, data):
        node = MyNode()
        node.data = data
        node.next = None
        self.__size+=1
        if self.__head is None:
            self.__head = node
        else:
            prev = self.__head
            while prev.next is not None:
                prev = prev.next
            prev.next = node


    def removeAt(self,index):
        if index == 0:
            self.__head = self.__head.next
            self.__size-=1
        else:
            temp = self.__head
            temp2 = None
            for i in range(index-1):
                temp = temp.next
            temp2 = temp.next
            temp.next = temp2.next
            self.__size -= 1
            temp2.next = None




        node = MyNode()
        





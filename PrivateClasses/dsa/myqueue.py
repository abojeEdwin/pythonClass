class MyQueue:
    def __init__(self,capacity):
        self.__head = self.__size = 0
        self.__tail = self.__capacity = - 1
        self.__queue = [None] * capacity
        self.__capacity = capacity
        self.__size = 0


    def enterQueue(self, value):
        if self.isFull():
            raise IndexError("Queue is full")
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__queue[self.__tail] = value
        self.__size += 1

    def isEmpty(self) -> bool:
        return self.__size == 0

    def getSize(self):
        return self.__size

    def show(self):
        for i in range(self.__size):
            print(self.__queue[i])

    def remove(self):
        if self.isEmpty():
            self.__head = self.__head % self.__capacity
            self.__size -= 1
        raise ValueError("Queue is empty")

    def isFull(self):
        return self.__size == self.__capacity
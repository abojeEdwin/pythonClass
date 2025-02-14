class MyStack:
    def __init__(self,capacity):
        self.__stack = [None] * capacity
        self.__top = 0
        self.__size = 0
        self.__capacity = capacity

    def push(self, value):
        if self.isEmpty():
            self.__top = (self.__top + 1) % self.__capacity
            self.__stack[self.__top + 1] = value
            self.__size += 1

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size


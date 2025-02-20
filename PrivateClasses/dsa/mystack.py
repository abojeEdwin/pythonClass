class MyStack:
    def __init__(self,size):
        self.__stack = [None] * size
        self.__top = 0
        self.__size = 0
        self.__capacity = size

    def push(self, value):
            self.__top = (self.__top + 1) % self.__capacity
            self.__stack[self.__top + 1] = value
            self.__size += 1

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        self.__stack[self.__top] = None
        self.__size -= 1

    def display(self):
       for item in self.__stack:
            print(item)




class MyStack:
    def __init__(self,size):
        self.__stack = [None] * size
        self.__top = 0
        self.__size = 0
        self.__capacity = size

    def push(self, value):
            self.__stack[self.__top] = value
            self.__top = (self.__top + 1) % self.__capacity
            self.__size += 1

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        self.__top -= 1
        value = self.__stack[self.__top]
        self.__stack[self.__top] = None
        self.__size -= 1
        return value

    def display(self):
       for item in self.__stack:
            print(item)

    def peek(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        print (self.__stack[self.__top-1])



class MyArray:
    def __init__(self,size):
        self.__size = 0
        self.__capacity = size
        self.__array = []

    def add(self, value):
        if self.isFull():
            raise IndexError ("Array is full")
        self.__array += value
        self.__size += 1

    def getSize(self):
        return self.__size

    def remove(self):
        if self.isEmpty():
            raise ValueError("Array is empty")
        for i in range(len(self.__array)):
            if self.__array[i] is not None:
                self.__array[i] = 0
        self.__size -= 1

    def isContain(self, value):
        for i in range(len(self.__array)):
            if self.__array[i] == value:
                return True
        return False

    def getCapacity(self):
        return self.__capacity

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def isFull(self):
        return self.__size == self.__capacity
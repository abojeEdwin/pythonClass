class MyQueue :

def __init__(self, size):
    size = 0


def isEmpty() :
    return size() == 0

def size() :
    return size

def enterQueue(item):
    if(!isFull()):
        queue[tail] = item
        tail = tail + 1 % 5
        size+1

    else :
        print("Queue is full")


def monstrar():
        for i in size:
            print(queue[(head + i) %5 ] + " ")



def deQueue():
    item = queue[head]
    if(!isEmpty()):
        head = head + 1 % 5
        size-1
    else:
        print("Queue is empty")
        return item

def isFull():
    return size() == 5

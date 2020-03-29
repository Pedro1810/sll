class Node:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data
    data = property(get_data, set_data)

    def set_next(self, node):
        self.__next = node
    def get_next(self):
        return self.__next
    next = property(get_next, set_next)

class SingleLinkedList:

    def __init__(self):
        self.__head = None
        self.__size = 0

    def __inc(self): self.__size += 1

    def __dec(self): self.__size -= 1

    def isempty(self):
        return self.__head is None

    def size(self):
        return self.__size
    def count(self):
        return self.size()

    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node
        self.__inc()
        return self

    def get(self, index):
        last = self.__head
        nodeIndex = 0
        while nodeIndex <= index:
            if nodeIndex == index:
                return last.data
            nodeIndex += 1
            last = last.next

    def contains(self, item):
        last = self.__head
        while last:
            if item == last.data:
                return True
            else:
                last = last.next
        return False

    def index(self, item):
       last = self.__head
       nodeIndex = 0
       while last:
           if last.data == item:
               return nodeIndex
           nodeIndex += 1
           last = last.next

    def __getitem__(self, index):
        if index >= self.__size:
            raise IndexError()
        return self.get(index)



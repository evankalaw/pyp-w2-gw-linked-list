from interface import AbstractLinkedList

from node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = elements
        self.start = None
        self.end = None

        if self.elements:
            for elem in self.elements:
                self.append(elem)
    
    def __str__(self):
        if self.start:
            result = [self.__getitem__(ind).elem for ind in range(len(self))]
            return str(result)
        else:
            return ''

    def __len__(self):
        if self.start:
            lenNode = self.start
            counter = 1
            while lenNode.next:
                counter += 1
                lenNode = lenNode.next
            return counter
        else:
            return 0

    def __iter__(self):
        pass

    def __getitem__(self, index):
        if self.start:
            getNode = self.start
            for i in range(index):
                getNode = getNode.next
            return getNode
        else:
            return None

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        self.append(LinkedList(other).start)

    def __eq__(self, other):
        return str(self) == str(other)
    
    def append(self, elem):
        appNode = Node(elem)
        if self.start == None and self.end == None:
            self.start = appNode
            self.end = appNode
        else:
            self.end.next = appNode
            self.end = appNode

    def count(self):
        return len(self)

    def pop(self, index=None):
        maxIndex = self.count() - 1
        if index:
            poppedNode = self.__getitem__(index)
        if index >=0 and index <= maxIndex:
            self.end = self.__getitem__(index + 1)
            self.__getitem__(index - 1).next = self.end
        elif index == maxIndex: #last index C: added the case when they dont enter an index to pop  or index == None
            self.end = self.__getitem__(index - 1)
            self.end.next = None
        else:
            index = maxIndex
            poppedNode = self.__getitem__(index).elem
            self.end = self.__getitem__(index - 1)
            self.__getitem__(index - 1).next
        return poppedNode
        

########## RUN ME PLZ #############
LL = LinkedList()
print('&' + str(LL) + '&')
LL.append(1)
LL.append(5)
LL.append(0)
LL.append(3)
LL.append(6)
LL.append(7)
print(str(LL))
print('length of LL: ', len(LL))
LL2 = LinkedList([2,3,5,8])
print(str(LL2))
print('length of LL2: ', LL2.count())
print(LL == LinkedList([1,5,0,3,6,7]))
LL.pop(3)
print(LL)
#######################################

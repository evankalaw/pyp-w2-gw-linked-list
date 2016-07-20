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
            return '[]'

    def __len__(self):
        if self.start:
            lenNode = self.start
            counter = 1
            while lenNode.next:
                counter += 1
                lenNode = lenNode.next
            return counter
        else:
            print(0)
            return 0

    def __iter__(self):
        pass

    def __getitem__(self, index):
        if self.start:
            if index < 0:
                index = len(self)-1
            getNode = self.start
            for i in range(index):
                getNode = getNode.next
            return getNode
        else:
            return None

    def __add__(self, other):
        new_list = LinkedList()
        if self.elements:
            for elem in self.elements:
                new_list.append(elem)
        if other.elements:
            for item in other.elements:
                new_list.append(item)
        return new_list

    def __iadd__(self, other):
        return self + other

    def __eq__(self, other):
        return str(self) == str(other)
    
    def __ne__(self, other):
        return str(self) != str(other)
    
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

    # def pop(self, index=None):
    #     maxIndex = self.count() - 1
    #     if (self.start == None and self.end == None) or index > maxIndex:
    #         raise IndexError
    #     if len(self) == 1:
    #         poppedNode = self.__getitem__(0).elem
    #         self.start = None
    #         self.end = None
    #         return poppedNode
    #     if index != None:
    #         poppedNode = self.__getitem__(index).elem
    #     if index == 0:
    #         self.start = self.__getitem__(index + 1)
    #     elif index > 0 and index <= maxIndex:
    #         print("i go here 4")
    #         self.end = self.__getitem__(index + 1)
    #         self.__getitem__(index - 1).next = self.end
    #     elif index == maxIndex or index == None: #last index Chris: added the case when they dont enter an index to pop and if index = 0 
    #         print("i go here 5")
    #         poppedNode = self.__getitem__(maxIndex).elem
    #         self.end = self.__getitem__(maxIndex - 1)
    #         self.end.next = None
    #     print(poppedNode)
    #     return poppedNode
    def pop(self, index=None):
        lenLL = self.count()
        maxIndex = lenLL - 1
        if index == None: #index is None
            index = maxIndex
        if lenLL == 0 or (index < 0 or index > maxIndex): #empty LL or index out of range
            raise IndexError
        elif lenLL == 1: #popping 1 element LL
            poppedNode = self.start
            self.start = None
        else: #popping multi-elem LL
            if index == 0: #popping the first elem
                poppedNode = self.__getitem__(index)
                self.start = self.__getitem__(index+1)
            elif index == maxIndex:  #popping the last elem
                poppedNode = self.__getitem__(index)
                self.end = self.__getitem__(index - 1)
                self.end.next = None
            else: # popping a middle elem
                poppedNode = self.__getitem__(index)
                self.__getitem__(index-1).next = self.__getitem__(index + 1)
        return poppedNode.elem  

########## RUN ME PLZ #############
LL = LinkedList()
print('&' + str(LL) + '&')
LL.append(1)
LL.append(5)
LL.append(0)
LL.append(3)
LL.append(6)
LL.append(7)
print('LL= ',str(LL))
print('length of LL: ', len(LL))
LL2 = LinkedList([2,3,5,8])
print('LL2 = ',str(LL2))
print('length of LL2: ', LL2.count())
print(LL == LinkedList([1,5,0,3,6,7]))
print('popping LL[3]: ', LL.pop(3))
print(LL)
print('popping LL[start]: ', LL.pop(0))
print(LL)
print('popping LL[end]: ', LL.pop(len(LL)-1))
print(LL)
print('popping LL[None]: ', LL.pop())
print(LL)
print('popping LL[None]: ', LL.pop())
print(LL)
print('popping LL[None]: ', LL.pop())
print(LL)
# LL = LinkedList()
# print('&' + str(LL) + '&')
# LL.append(1)
# LL.append(5)
# LL.append(0)
# LL.append(3)
# LL.append(6)
# LL.append(7)
# print(str(LL))
# print('length of LL: ', len(LL))
# LL2 = LinkedList([2,3,5,8])
# print(str(LL2))
# print('length of LL2: ', LL2.count())
# print(LL == LinkedList([1,5,0,3,6,7]))
# LL.pop(0)
# print(LL)
# ## CHRIS TESTS ##
# print("Chris down here - single list pop")
# LL3 = LinkedList([9])
# LL3.pop()
# LL3.start
# LL3.end
# print("this is empty:",LL3)
# LL3.count()
# print("Chris down here - errors raised")
# LL4 = LinkedList()
# LL4.pop()
# print("Chris down here - adding shizzs")
# L1 = LinkedList([1,5,0,3,6,7])
# print(L1)
# L2 = LinkedList([9,0])
# #print(LinkedList([1,5,0,3,6,7]) + LinkedList([9,0]))
# new = L1 + L2
# dup_list = LinkedList([1, 5, 0, 3, 6, 7, 9, 0])
# print(dup_list == new)
# print("Chris down here - add: trying with test cases")
# my_list = LinkedList()
# print(my_list)
# new_list = my_list + LinkedList([1])
# print(my_list)
# print(my_list == LinkedList([1]))
#print(new)
# new.start.next
#assert LinkedList([1,5,0,3,6,7]) + LinkedList([9,0]) == LinkedList([1,5,0,3,6,7,9,0])
#######################################

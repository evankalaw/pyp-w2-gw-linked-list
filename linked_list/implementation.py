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

        #############################################
        # DON'T NEED ANY OF THIS.......
        # self.nodeList = []                
        #     if len(self.elements) == 1:
        #       newNode = Node(self.elements[0])
        #       self.start = newNode
        #       self.end = newNode
        #     if len(self.elements) > 1:
        #         for index in range(len(elements)):
        #             self.noded_list.append(Node(self.elements[index]))
        #         self.start = self.noded_list[0]
        #         self.end = self.noded_list[-1]
        #         for index in range(len(self.noded_list)-1):
        #             self.noded_list[index].next = self.noded_list[index+1]
    
    # def __init__(self, elements=None):
    #     self.elements = elements
    #     self.start = None
    #     self.end = None
    #     self.noded_list = []
    #     if elements:
    #         for index in range(len(self.elements)):
    #             if index == 0:
    #                 new_node = Node(self.elements[index],self.end)
    #                 self.noded_list.append(new_node)
    #                 self.start = new_node
    #             else:
    #                 new_node = Node(self.elements[index],self.end)
    #                 self.noded_list.append(new_node)
    #                 self.noded_list[index-1].next=new_node
    #                 self.end = new_node
    ##################################################################
    
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

        # self.noded_list.append(addedNode)
        # if len(self.noded_list) < 2:
        #     self.start = addedNode
        #     self.end = addedNode
        # else:
        #     self.end = addedNode
        #     self.noded_list[-2].next = self.end

        # if self.start == None:
        #     self.start = addedNode
        # if self.end != None:
        #     self.end.next = addedNode
        # self.end = addedNode
        # self.noded_list[-1].next = 

    def count(self):
        return len(self)

    def pop(self, index=None):
        maxIndex = self.count() - 1
        if index >=0 and index <= maxIndex:
            self.end = self.__getitem__(index + 1)
            self.__getitem__(index - 1).next = self.end
        elif index == maxIndex: #last index
            self.end = self.__getitem__(index - 1)
            self.end.next = None
        else:
            raise

    # # our own methods defined down here (for now)
    # def start(self):
    #     pass
    
    # def end(self):
    #     return self[-1].next
        

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

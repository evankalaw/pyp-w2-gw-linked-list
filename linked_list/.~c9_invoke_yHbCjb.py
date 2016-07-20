from .interface import AbstractLinkedList

from node import Node

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.elements = elements
        self.start = None
        self.end = None
        self.nodeList = []
        if elements != None:
            
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
        
    #         print(index
                self.nodeList += [Node(elem)]
            for index in range(len(self.elements)-1): #1st to 2nd
                self.nodeList[index].next = self.nodeList[index+1]
    
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
        
    def __str__(self):
        return str(self)

    def __len__(self):
        return len(self.nodeList)

    def __iter__(self):
        pass

    def __getitem__(self, index):
        return self.nodeList[index]

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        return self == other

    def append(self, elem):
        addedNode = Node(elem)
        if self.start == None and self.end == None:
            self.start = addedNode
            self.end = addedNode
        else:
            self.end.next = addedNode
            self.end = addedNode
        
        self.nodeList += [addedNode]
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
        pass

    def pop(self, index=None):
        pass
    # # our own methods defined down here (for now)
    # def start(self):
    #     pass
    
    # def end(self):
    #     return self[-1].next
        

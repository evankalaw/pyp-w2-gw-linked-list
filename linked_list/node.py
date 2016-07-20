class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem=None, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.elem == other.elem
        else:
            return False

    def __repr__(self):
        return str(self)
        

    
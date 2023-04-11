"""
A doubly linked list class using a node class. Each node has a value, a previous reference
and a next reference. Different methods can be called that allow nodes to be added and
searched for.

File Name: doubly_linked_list.py
Author: Caleb Smith
Collaborators: None
Internet Sources: None
"""

# An individual node in a DoublyLinkedList.
# value: reference to the value stored in the node
# next: reference to the next node
# prev: reference to the previous node in the list
class Node:
    def __init__(self, v, p, n):
        self.value = v
        self.prev = p
        self.next = n
    
    def __str__(self):
       return str(self.value)

# A DoublyLinkedList data structure with sentinel nodes
# sentiel nodes header and trailer store None as values and are not part of the list
# The purpose of the sentiel nodes is to ensure all adds and removes are happening beteween two nodes
# (eliminates all special cases)
class DoublyLinkedList:
   
    def __init__(self):
        self.header = Node(None, None, None)
        self.trailer = Node(None, self.header, None)
        self.header.next = self.trailer
        self.size = 0

    #adds the value v between nodes n1 and n2
    def add_between(self, v, n1, n2):
        if n1 is None or n2 is None:
            raise ValueError("Invalud n1 or n2 - can't be None")
        if n1.next is not n2:
            raise ValueError("Second node must come before first node")
        
        #step 1: make a new node
        new_node = Node(v, n1, n2)
        
        #step 2: fix n1.next and n2.prev
        n1.next = new_node
        n2.prev = new_node

        #step 3: increment size
        self.size += 1

    def add_first(self, v):
        """
            parameters:
                v: type is the generic type E of the list
            return:
                None
            adds a the value v at the head of the list
        """
        self.add_between(v, self.header, self.header.next)
        self.size += 1

    def add_last(self, v):
        """
            parameters:
                v: type is the generic type E of the list
            return value:
                None
            adds a the value v at the tail of the list
        """
        self.add_between(v, self.trailer.prev, self.trailer)
        self.size += 1

    def __str__(self):
        return_string = "["

        if self.header.next is not self.trailer:
            temp_node = self.header.next
            while temp_node.next is not self.trailer:
                return_string += f"{temp_node.value} "
                temp_node = temp_node.next
            return return_string + f"{temp_node.value}]"

    def search(self, v)->int:
        temp_node = self.header
        index = -1
        
        while temp_node.next is not self.trailer:
            temp_node = temp_node.next
            index += 1

            if temp_node.value == v:
                return index
            
        return -1
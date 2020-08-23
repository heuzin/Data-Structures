"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # if no head / empty list:
        if self.head is None:
            # create new node
            new_node = ListNode(value)
            # set self.head to new_node
            self.head = new_node
            # set self.tail to new_node
            self.tail = new_node
            self.length += 1
        else:
            # create new node
            new_node = ListNode(value, None, self.head)
            # set self.head to new_node
            self.head = new_node
            self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail is None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = ListNode(value, self.tail, None)
            old_tail = self.tail
            old_tail.next = new_node
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value
        else:
            current_tail = self.tail
            new_tail = current_tail.prev
            self.tail = new_tail
            new_tail.next = None
            self.length -= 1
            return current_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return 
        node_value = node.value
        # delete the node
        self.delete(node)
        self.add_to_head(node_value)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return 
        node_value = node.value
        # delete the node
        self.delete(node)
        self.add_to_tail(node_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        elif self.head == node:
            removed_node = self.head
            self.head = node.next
            return removed_node
        elif self.tail == node:
            removed_node = self.tail
            self.tail = node.prev
            return removed_node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass
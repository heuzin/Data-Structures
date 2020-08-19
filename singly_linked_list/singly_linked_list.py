class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next # The next node in the list

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self,value):
        # check if there's a tail
        # If there is no tail (empty list)
        if self.tail is None:
            # create a new node
            new_tail = Node(value, None)
            # Set self.head and self.tail to new node
            self.head = new_tail
            self.tail = new_tail
        # If there is a tail (general case):
        else:
            # create a new node with the value we want to add, next = None
            new_tail = Node(value, None)
            # set current tail.next to the new node
            old_tail = self.tail
            old_tail.next = new_tail
            # set self.tail to the new node
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        # if not head (empty list)
        if self.head is None: # if self.head i none
            return None
        #list with one element
        if self.head == self.tail:
            # set self.head to current_head.next / None
            current_head = self.head
            self.head = None
            # set self.tail to none
            self.tail = None
            # Decrement length by 1
            self.length -= 1
            return current_head.value
        # If head (General case):
        else:
            # set self.head to current_head.next
            current_head = self.head
            self.head = current_head.next
            # return current_head.next
            self.length -= 1
            return current_head.value
            
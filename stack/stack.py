"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# from singly_linked_list.singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return
        
        else:
            item = self.stack[len(self.stack) - 1]
            self.stack.remove(item)
            return item

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.add_to_head(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         return self.storage.remove_head()
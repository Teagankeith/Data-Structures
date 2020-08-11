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
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = [] 

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else: 
#             self.size -= 1
#             return self.storage.pop()

from singly_linked_lists import LinkedList


class Stack:
    def __init__(self):
        self.length = 0
        self.storage = LinkedList()
    def __len__(self):
        return self.length
    def push(self, value):
        self.length += 1
        self.storage.add_to_tail(value)
    
    def pop(self):
        if self.length == 0:
            return None  
        # Assign the indice removed to a variable and remove it
        remove_tail: self.storage.remove_tail()
        # Remove 1 from the length of the LinkedList
        self.length -= 1
        # Return the remove indice from the list
        return remove_tail 

    

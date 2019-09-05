import sys;

sys.path.append('../')

from doubly_linked_list import *

class Queue:
  def __init__(self):
    self.size = 0

    self.storage = DoublyLinkedList()

  def enqueue(self, item):
    self.storage.add_to_head(item)

  def dequeue(self):
    return self.storage.remove_from_tail()

  def len(self):
    return self.storage.__len__()


# Queue using array

# class Queue:
#   def __init__(self):
#     self.size = 0
#     self.storage = []

#   def enqueue(self, item):
#     self.storage.append(item)

#   def dequeue(self):
#     if len(self.storage) > 0:
#       return self.storage.pop(0)

#   def len(self):
#     return len(self.storage)

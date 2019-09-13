class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    parent = (index - 1) // 2

    if index <= 0 or self.storage[index] < self.storage[parent]:
      return

    tmp = self.storage[parent]
    self.storage[parent] = self.storage[index]
    self.storage[index] = tmp
    self._bubble_up(parent)

  def _sift_down(self, index):
    left_node = (index * 2) + 1
    right_node = (index * 2) + 2
    highest_val_index = 0

    if self.storage[left_node] > self.storage[right_node]:
      highest_val_index = left_node
    else:
      highest_val_index = right_node

    if self.storage[highest_val_index] < self.storage[index]:
      return
    else:
      tmp = self.storage[index]
      self.storage[index] = self.storage[highest_val_index]
      self.storage[highest_val_index] = tmp
      self._sift_down(highest_val_index)
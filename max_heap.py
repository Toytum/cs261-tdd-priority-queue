# MaxHeap: A binary 'max' heap.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_max_heap.py.
# Ethan Weikel

class MaxHeap:

   def __init__(self):
      self._data = []

   def _size(self):
      return len(self._data)

   def _is_empty(self):
      return self._size() == 0

   def _last_index(self):
      return int(self._size()-1)

   def _value_at(self, index):
      return self._data[index]

   def _left_child_index(self, index):
      return (index * 2) + 1
      
   def _left_child(self,index):
      if self._left_child_index(index) >= self._size():
         return None
      else:
         return self._data[self._left_child_index(index)]
   
   def _has_left_child(self, index):
      return self._left_child(index) != None

   def _right_child_index(self, index):
      return (index * 2) + 2

   def _right_child(self, index):
      if self._right_child_index(index) >= self._size():
         return None
      else:
         return self._data[self._right_child_index(index)]
   
   def _has_right_child(self, index):
      return self._right_child(index) != None
   
   def _parent_index(self, index):
      if index == 0:
         return -1
      elif 0 < index < 3:
         return 0
      elif ((index - 1) / 2).is_integer():
         return int((index -1) / 2)
      else:
         return int((index -2) / 2)

   def _parent(self, index):
      return self._data[int(self._parent_index(index))]

   def _greater_child_index(self, index):
      if not self._has_left_child(index) and self._has_right_child(index):
         return None

      elif self._has_left_child(index) and not self._has_right_child(index):
         return self._left_child_index(index)

      elif self._has_left_child(index) and self._has_right_child(index):
         if self._left_child(index) >= self._right_child(index):
            return self._left_child_index(index)
         else:
            return self._right_child_index(index)

   def _obeys_heap_property_at_index(self, index):
      if self._size() == 1:
         return True
      elif self._has_left_child(index) and not self._has_right_child(index):
         return self._value_at(index) > self._left_child(index)
      elif self._has_left_child(index) and self._has_right_child(index):
         return self._value_at(index) > self._left_child(index) and self._value_at(index) > self._right_child(index)
      else:
         return True

   def _swap(self, indexA, indexB):
      temp = self._data[indexA]
      self._data[indexA] = self._data[indexB]
      self._data[indexB] = temp

   def _sift_down(self, index):
      if not self._has_left_child(index) and not self._has_right_child(index):
         return self

      elif self._has_left_child(index) and self._has_right_child(index):
         if self._value_at(index) < self._left_child(index) and self._value_at(index) < self._right_child(index):

            if self._left_child(index) < self._right_child(index):
               self._swap(index, self._right_child_index(index))
               return self._sift_down(self._right_child_index(index))

            elif self._left_child(index) > self._right_child(index):
               self._swap(index, self._left_child_index(index))
               return self._sift_down(self._left_child_index(index))

         elif not self._value_at(index) < self._left_child(index) and self._value_at(index) < self._right_child(index):
               self._swap(index, self._right_child_index(index))
               return self._sift_down(self._right_child_index(index))
         
      elif self._has_left_child(index) and not self._has_right_child(index):
         if self._value_at(index) < self._left_child(index):
            self._swap(index, self._left_child_index(index))
            return self._sift_down(self._left_child_index(index))
      
      elif self._has_right_child(index) and not self._has_left_child(index):
         if self._value_at(index) < self._right_child(index):
            self._swap(index, self._right_child_index(index))
            return self._sift_down(self._right_child_index(index))

   def _sift_up(self, index):
      if index == 0:  
         return self._data[index]
      elif self._value_at(index) > self._parent(index):
         self._swap(index, self._parent_index(index))
         self._sift_up(self._parent_index(index))
      
   def insert(self, item):
      self._data.append(item)
      self._sift_up(self._last_index())

   def delete(self):
      if self._size() == 0:
         return None
      elif self._size() == 1:
         toReturn = self._data[0]
         self._data.pop()
         self._sift_down(0)
         return toReturn
      else:
         toReturn = self._data[0]
         self._swap(0, self._last_index())

         self._data.pop()
         self._sift_down(0)
         return toReturn

   pass

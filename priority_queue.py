# PriorityQueue: An efficient priority queue.
# If you use a binary heap, it'll do most of the work, leaving this
# implementation quite trivial.
# Your implementation should pass the tests in test_priority_queue.py.
# Ethan Weikel

from max_heap import MaxHeap

class PriorityQueue:

    def __init__(self):
        self.heap = MaxHeap()

    def enqueue(self, job):
        self.heap.insert(job)

    def dequeue(self):
        return self.heap.delete()

    def is_empty(self):
        return self.heap._is_empty()
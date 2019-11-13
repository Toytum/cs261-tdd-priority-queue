# NaivePriorityQueue (aka 'ShittyQueue'): A simple but inefficient priority queue.
# Your implementation should pass the tests in test_naive_priority_queue.py.
# Ethan Weikel

class NaivePriorityQueue:

    def __init__(self):
        self.data = []
        pass

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop()


    

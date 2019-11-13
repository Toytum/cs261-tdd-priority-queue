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
        if self.is_empty():
            return None
        else:
            highest_priority = self.data[0]
            for job in self.data:
                if job > highest_priority:
                    highest_priority = job
            self.data.remove(highest_priority)
            return highest_priority

    def is_empty(self):
        return len(self.data) == 0



    

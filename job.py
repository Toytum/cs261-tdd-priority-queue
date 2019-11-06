# Job: A process or task that has a priority.
# Your implementation should pass the tests in test_job.py.
# YOUR NAME

class Job:

    def __init__(self, p = None, m = None):
        self.priority = p
        self.message = m
        pass

    def __eq__(self, other):
        return self.priority == other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __gt__(self, other):
        return self.priority > other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __repr__(self):
        pass

    def __str__(self):
        pass    


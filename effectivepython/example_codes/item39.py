# Example 01
class InputData:
    def read(self):
        raise NotImplementedError


# Example 02
class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()


# Example 03
class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


# Example 04
class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('¥n')
    
    def reduce(self, other):
        self.result += other.result
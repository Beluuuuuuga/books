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
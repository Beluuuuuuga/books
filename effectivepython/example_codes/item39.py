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


# Example 05
import os

def generate_inputs(data_dir):
    for name in os.listdir(data_dir): # ディレクトリ直下のファイルを取得
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(inputs_list):
    workers = []
    for input_data in inputs_list:
        workers.append(LineCountWorker(input_data))
    return workers

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers] # map関数使用
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

import os
import random

def write_test_files(tmpdir):
    os.mkdir(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('¥n' * random.randint(1, 100))

tmpdir = 'test_inputs'
# write_test_files(tmpdir)
result = mapreduce(tmpdir)
print(f'There are {result} lines')


# Example 06
class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData2(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker2(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('¥n')
    
    def reduce(self, other):
        self.result += other.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

config = {'data_dir': tmpdir}
result = mapreduce(LineCountWorker2, PathInputData2, config)
print(f'There are {result} lines')
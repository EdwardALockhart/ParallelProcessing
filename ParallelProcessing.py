# Single Function Arguments
def func(a):
    return a*a
res = exec.map(func, a_list)

# Multiple Function Arguments
def func(a, b):
    return a*b
res = exec.starmap(func, zip(a_list, b_list))
from itertools import repeat
res = exec.starmap(func, zip(a_list, repeat(b_list)))



# Number of CPUs
import multiprocessing
n_cpus = multiprocessing.cpu_count()-1



# Linux
# Usage Example
def func1(data):
    return data*2

def func2(data):
    return data/2
    
from concurrent.futures import ProcessPoolExecutor
def multiprocessing(func, task_chunks, workers):
    # For CPU heavy tasks
    # func - function to run
    # task_chunks - iterable to be processed
    # workers - number of workers
    with ProcessPoolExecutor(workers) as exec:
        res = exec.map(func, task_chunks)
    return list(res)

results1 = multiprocessing(func1, task_chunks, n_cpus)

from concurrent.futures import ThreadPoolExecutor
def multithreading(func, task_chunks, workers):
    # For input/output heavy tasks
    # func - function to run
    # task_chunks - iterable to be processed
    # workers - number of workers
    with ThreadPoolExecutor(workers) as exec:
        res = exec.map(func, task_chunks)
    return list(res)

results2 = multithreading(func2, task_chunks, n_cpus)



# Windows
# Code before "if __name__ == '__main__':" runs for all child processes (the workers)
# Define the fuctions for all child processes before "if __name__ == '__main__':"
# When running, ensure that all data required to complete the task are in task_chunks

# Usage Example
def func1(data):
    return data*2

def func2(data):
    return data/2

if __name__ == '__main__':
    # Code run here runs only on the parent script
    from multiprocessing import Pool
    with Pool(processes = n_cpus) as pool:
        results1 = pool.map(func1, task_chunks)
        
    with Pool(processes = n_cpus) as pool:
        results2 = pool.map(func2, task_chunks)

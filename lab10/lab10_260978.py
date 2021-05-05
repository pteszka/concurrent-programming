#!/usr/bin/env python3

import numpy as np 
import threading

DETERMINANT=0

# MATRIX=np.matrix([[3, 2, 1, 2], 
#                 [4, 3, 2, 1],
#                 [1, 2, 2, 5],
#                 [1, 6, 0, 1]])

# MATRIX=np.matrix([[1, 1, 1, 1], 
#                 [1, 1, 1, 1],
#                 [1, 2, 2, 5],
#                 [0, 0, 0, 0]])

MATRIX=np.matrix([[0, 1, 2, 7], 
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [-1, 1, -1, 1]])


def divide_into_matrices():
    res = []
    x = 1
    for idx, m in enumerate(MATRIX[0].A1):
        if m == 0:
            x *= -1
            pass
        else:
            selector = [0, 1, 2, 3]
            selector.remove(idx)
            res.append((m, x, MATRIX[1:, selector]))
            x *= -1
    return res

def make_threads(arr, lock):
	res = []
	for x in arr:
		res.append(threading.Thread(target=thread_task, args=(x, lock)))
	return res

def add_columns(matrix):
    columns_to_be_added = np.array(matrix[:, :-1])
    matrix = np.hstack((matrix, columns_to_be_added))
    return matrix

def thread_task(data, lock):
    global DETERMINANT
    
    lock.acquire()
    m, x, matrix = data
    DETERMINANT += sarus(m*x, matrix)
    lock.release()

def sarus(multi, matrix):
    matrix = add_columns(matrix)
    a = 0
    b = 0
    for idx, _ in enumerate(matrix):
        a += matrix[0,idx]*matrix[1,idx+1]*matrix[2,idx+2]
        b += matrix[0,idx+2]*matrix[1,idx+1]*matrix[2,idx]
    return multi*(a-b)

def join_threads(threads):
	for t in threads:
		t.join()

def start_threads(threads):
	for t in threads:
		t.start()

def calculateDeterminant():
    global DETERMINANT
    DETERMINANT=0

    arr = divide_into_matrices()

    lock = threading.Lock()
    threads = make_threads(arr, lock)
    
    start_threads(threads)
    join_threads(threads)

    print(DETERMINANT)

if __name__ == "__main__":
    calculateDeterminant()
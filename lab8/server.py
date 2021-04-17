import threading
import sys

SUM=0

def increment(x):
    global SUM
    SUM += x

def thread_task(arr, lock):
    lock.acquire()
    increment(sum(arr))
    lock.release()

def join_threads(threads):
	for t in threads:
		t.join()

def start_threads(threads):
	for t in threads:
		t.start()

def make_threads(arr, n, lock):
	res = []
	for x in get_part_of_list(arr, n):
		res.append(threading.Thread(target=thread_task, args=(x, lock)))
	return res

def get_part_of_list(arr, num_threads):
    k, m = divmod(len(arr), num_threads)
    return list(arr[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(num_threads))

def main():
	global SUM 
	SUM=0


	lock = threading.Lock()

	arr = [i for i in range(8436378)]
	n = int(input("Podaj liczbę wątków: "))

	threads = make_threads(arr, n, lock)
	start_threads(threads)
	join_threads(threads)

	print(f"Wynik spodziewany: {sum(arr)}\nWynik obliczony przez wątki: {SUM}")

if __name__ == "__main__":
	main()
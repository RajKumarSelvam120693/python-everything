import threading
import time


def print_num():
    for i in range(0,5):
        time.sleep(2)
        print(f"{i}")

def print_letters():
    for i in "abcdef":
        time.sleep(2)
        print(f"{i}")

t = time.time()
# below if you use print_num() then the threading will be executed sequential and not concurrent
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letters)
# start the threads concurrently
t1.start()
t2.start()
# join the threads to the main thread
t1.join()
t2.join()
finished_time = time.time() - t
print(finished_time)
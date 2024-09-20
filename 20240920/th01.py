import time
import threading

def print_numbers():
    thread_id = threading.get_ident()
    for i in range(3):
        print(f'{i}@{thread_id}')
        # time.sleep(0.025)

threads=[]
for i in range(3):
    thread = threading.Thread(target=print_numbers)
    threads.append(thread)
    thread.start()  # Start the thread
for i in range(3):
    thread.join()   # Wait for the thread to finish

print_numbers()
""" import time
import threading

def print_numbers():
    thread_id = threading.get_ident()
    for i in range(5):
        print(f'@{thread_id}:{i}')
        time.sleep(1)



thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)
thread1.start()  # Start the thread
thread2.start()  # Start the thread
#thread1.join()   # Wait for the thread to finish
#thread2.join()   # Wait for the thread to finish
print_numbers() """
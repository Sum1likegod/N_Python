# import threading
# import time as t
# def thread_task(task):
#     # Do some work here
#     print("Task processed:", task)

# tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# t1 = t.perf_counter()
# # if __name__ == '__main__':
# #     tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #     threads = []
# #     for task in tasks:
# #         thread = threading.Thread(target=thread_task, args=(task,))
# #         threads.append(thread)
# #         thread.start()
# #     for thread in threads:
# #         thread.join()

# thru_mapping = map(thread_task, tasks)
# print(thru_mapping)
# t2 = t.perf_counter()
# print(t2 - t1)


# import threading

# def increment(counter, lock):
#     for i in range(10000):
#         lock.acquire()
#         counter += 1
#         lock.release()

# if __name__ == '__main__':
#     counter = 0
#     lock = threading.Lock()

#     threads = []
#     for i in range(2):
#         thread = threading.Thread(target=increment, args=(counter, lock))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     print("Counter value:", counter)


import threading
def my_func():
    thread_name = threading.current_thread().name
    print("Hello from thread", threading.current_thread().name)
    return thread_name
thread = threading.Thread(target=my_func,name="test_thread")
# thread_name = threading.current_thread().name
thread.start()
thread.join()

print("Thread name:",thread.name)


# from multiprocessing import Process
# import logging
# from time import sleep

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)


# class MyProcess(Process):
#     def __init__(
#         self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None
#     ):
#         super().__init__(group=group, target=target, name=name, daemon=daemon)
#         self.args = args

#     def run(self) -> None:
#         logger.debug(self.args)


# def example_work(params):
#     sleep(0.5)
#     logger.debug(params)


# if __name__ == "__main__":
#     processes = []
#     for i in range(3):
#         pr = Process(target=example_work, args=(f"Count process function - {i}",))
#         pr.start()
#         processes.append(pr)

#     for i in range(2):
#         pr = MyProcess(args=(f"Count process class - {i}",))
#         pr.start()
#         processes.append(pr)

#     [el.join() for el in processes]
#     [print(el.exitcode, end=" ") for el in processes]
#     logger.debug("End program")



# from multiprocessing import Process, Value, RLock, current_process
# from time import sleep
# import logging
# import sys

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

# def worker(val: Value):
#     logger.debug(f'Started {current_process().name}')
#     sleep(1)
#     with val.get_lock():
#         val.value += 1
#     logger.debug(f'Done {current_process().name}')
#     sys.exit(0)

# if __name__ == '__main__':
#     lock = RLock()
#     value = Value('d', 0, lock=lock)
#     pr1 = Process(target=worker, args=(value, ))
#     pr1.start()
#     pr2 = Process(target=worker, args=(value, ))
#     pr2.start()

#     pr1.join()
#     pr2.join()

#     print(value.value)



# from multiprocessing import Process, RLock, current_process
# from multiprocessing.sharedctypes import Value, Array
# from ctypes import Structure, c_double
# import logging

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

# class Point(Structure):
#     _fields_ = [('x', c_double), ('y', c_double)]

# def modify(num: Value, string: Array, arr: Array):
#     logger.debug(f'Started {current_process().name}')
#     logger.debug(f"Change num: {num.value}")
#     with num.get_lock():
#         num.value **= 2
#     logger.debug(f"to num: {num.value}")
#     with string.get_lock():
#         string.value = string.value.upper()
#     with arr.get_lock():
#         for a in arr:
#             a.x **= 2
#             a.y **= 2
#     logger.debug(f'Done {current_process().name}')

# if __name__ == '__main__':
#     lock = RLock()
#     number = Value(c_double, 1.5, lock=lock)
#     string = Array('c', b'hello world', lock=lock)
#     array = Array(Point, [(1, -6), (-5, 2), (2, 9)], lock=lock)

#     p = Process(target=modify, args=(number, string, array))
#     p2 = Process(target=modify, args=(number, string, array))
#     p.start()
#     p2.start()
#     p.join()
#     p2.join()
#     print(number.value)
#     print(string.value)
#     print([(arr.x, arr.y) for arr in array])







# from multiprocessing import Process, Manager, current_process
# from random import randint
# from time import sleep
# import logging

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

# def worker(delay, val: Manager):
#     name = current_process().name
#     logger.debug(f'Started: {name}')
#     sleep(delay)
#     val[name] = current_process().pid
#     logger.debug(f'Done: {name}')

# if __name__ == '__main__':
#     with Manager() as manager:
#         m = manager.dict()
#         processes = []
#         for i in range(5):
#             pr = Process(target=worker, args=(randint(1, 3), m))
#             pr.start()
#             processes.append(pr)

#         [pr.join() for pr in processes]
#         print(m)





# from multiprocessing import Manager, Process
# import time

# def modify_first(shared_list):
#     shared_list[0]['key1'] = 'modified by first process'
#     print("First Process: Modified the first dictionary")

# def modify_third(shared_list):
#     shared_list[2]['key3'] = 'modified by third process'
#     print("Third Process: Modified the third dictionary")

# def read(shared_list):
#     # Чекаємо деякий час, щоб зміни були внесені
#     time.sleep(2)
#     readable_list = [dict(proxy_dict) for proxy_dict in shared_list]
#     print(f"Read Process: Read the shared list - {readable_list}")

# if __name__ == '__main__':
#     with Manager() as manager:
#         shared_list = manager.list([
#             {'key1': 'original1'},
#             {'key2': 'original2'},
#             {'key3': 'original3'}
#         ])
#         p1 = Process(target=modify_first, args=(shared_list,))
#         p2 = Process(target=modify_third, args=(shared_list,))
#         p3 = Process(target=read, args=(shared_list,))

#         p1.start()
#         p2.start()
#         p3.start()

#         p1.join()
#         p2.join()
#         p3.join()





# from multiprocessing import Pipe, Process, current_process
# from time import sleep
# import sys
# import logging

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

# recipient1, sender1 = Pipe()
# recipient2, sender2 = Pipe()

# def worker(pipe: Pipe):
#     name = current_process().name
#     logger.debug(f'{name} started...')
#     val = pipe.recv()
#     logger.debug(val**2)
#     sys.exit(0)

# if __name__ == '__main__':
#     w1 = Process(target=worker, args=(recipient1, ))
#     w2 = Process(target=worker, args=(recipient2, ))

#     w1.start()
#     w2.start()

#     sender1.send(8)
#     sleep(1)
#     sender2.send(16)





# from multiprocessing import Queue, Process, current_process
# from time import sleep
# import sys
# import logging

# logger = logging.getLogger()
# stream_handler = logging.StreamHandler()
# logger.addHandler(stream_handler)
# logger.setLevel(logging.DEBUG)

# q = Queue()

# def worker(queue: Queue):
#     name = current_process().name
#     logger.debug(f'{name} started...')
#     val = queue.get()
#     logger.debug(f'{name} {val**2}')
#     sys.exit(0)

# if __name__ == '__main__':
#     w1 = Process(target=worker, args=(q, ))
#     w2 = Process(target=worker, args=(q, ))

#     w1.start()
#     w2.start()

#     q.put(8)
#     sleep(1)
#     q.put(16)




from multiprocessing import JoinableQueue, Process, current_process
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

jq = JoinableQueue()

def worker(jqueue: JoinableQueue):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = jqueue.get()
    logger.debug(f'{name} {val**2}')
    sleep(1)
    jqueue.task_done()
    sys.exit(0)

if __name__ == '__main__':
    w1 = Process(target=worker, args=(jq, ))
    w2 = Process(target=worker, args=(jq, ))

    w1.start()
    w2.start()

    jq.put(8)
    sleep(1)
    jq.put(16)
    jq.join()
    print('Finished')

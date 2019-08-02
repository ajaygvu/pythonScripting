import queue
import threading


def basic_worker(q):
    while True:
        item = q.get()
        # do_work(item)
        print(item)
        q.task_done()


def basic():
    q = queue.Queue()
    for item in range(4):
        q.put(item)

    for i in range(3):
         t = threading.Thread(target=basic_worker,args=(q,))
         t.daemon = True
         t.start()

    q.join()       # block until all tasks are done
    print('got here')

basic()

'''

So when you comment out the daemon line, you'll notice that the program does not finish, you'll have to interrupt it manually. Setting the threads to daemon threads makes sure that they are killed once they have finished.

Note: you could achieve the same thing here without daemon threads, if you would replace the infinite while loop with another condition:

#t.daemon = True

def basic_worker(q):
        while not q.empty():
            item = q.get()
            # do_work(item)
            print(item)
            q.task_done()



'''
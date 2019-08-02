import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s' ,)

def wait_for_event(e):
    logging.debug('wait_for_event starting 1a')
    event_is_set = e.wait()
    logging.debug('event set1b: %s', event_is_set)

def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting 2a')
        event_is_set = e.wait(t)
        logging.debug('event set2b: %s', event_is_set)
        if event_is_set:
            logging.debug('processing event2c')
        else:
            logging.debug('doing other things2d')

if __name__ == '__main__':
    e = threading.Event()
    t1 = threading.Thread(name='blocking',
                          target=wait_for_event,
                          args=(e,))
    t1.start()

    t2 = threading.Thread(name='non-blocking',
                          target=wait_for_event_timeout,
                          args=(e, 2))
    t2.start()

    logging.debug('Waiting before calling Event.set()3a')
    time.sleep(20)
    e.set()
    logging.debug('Event is set3b')

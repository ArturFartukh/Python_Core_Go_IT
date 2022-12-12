from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.append(element)


def pop():
    return lifo.popleft()

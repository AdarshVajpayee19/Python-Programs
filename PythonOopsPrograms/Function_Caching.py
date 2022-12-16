import time
from functools import lru_cache


# lru_cache is an decorator.

# maxsize=3 means it saves previous Three values.
@lru_cache(maxsize=3)
def some_work(n):
    # some task taking n seconds.
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some Work.")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("Done....Calling Again")
    some_work(3)
    some_work(9)
    print("Called Again")

# saving Previous Sleep in cache  u can see in output console that after running program first line
# it prints other two lines Suddenly, because of cache.

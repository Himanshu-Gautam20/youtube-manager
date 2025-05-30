# implement a decorater that caches the return values of a function, so that when it called with the same arguments, the cached value returned instead of re-excuting the value

import time

def cache(func):
    cache_values = {}
    print(cache_values)
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(2, 5))
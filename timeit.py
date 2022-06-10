"""
This is a module that contains a method called timeit that can be used to time a function run

Usage: use as a wrapper around your function call

e.g.

@timeit
your_function_call (args, kwargs)

"""

from functools import wraps
import time

def timeit(func):
    
    # the advantage of using wraps is that
    # it copies metadata of inner function (function_timer) to the outer function
    # Without it, the decorated function object will reference the wrapper rather than the inner function
    # This helps in debugging
    # E.g. if we called help on the decorated function without the wraps, the help would be on the decorator instead of the inner function
    @wraps(func)
    def function_timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("func:{0} args:[{1}, {2}] took: {3:2.4}f sec".format(func.__name__, args, kwargs, end-start))
        return result
    return function_timer
import functools
import time


def time_it():
    def wrapper(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            print(f"{func} measurements:")
            start = time.time_ns()
            result = func(self, *args, **kwargs)
            end = time.time_ns()
            print(f"Time: {(end - start) / 1e9}s")
            print(f"Result: {result}")
            return result
        return wrap
    return wrapper

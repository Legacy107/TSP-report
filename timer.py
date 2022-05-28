import timeit

def timer_func_with_result(func):
    def function_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        runtime = timeit.default_timer() - start_time
        return (runtime, result)
    return function_timer

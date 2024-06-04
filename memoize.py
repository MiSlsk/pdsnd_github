import functools

def memoize(function):
    """Wrapper function to cache temporary results and speed up calculations."""
    function._cache = {}
            
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))

        if key in function._cache.keys():
            result = function._cache[key]
        else:
            result = function(*args, **kwargs)
            function._cache[key] = result
                                                                                         
        return result
                                                                                                                
    return wrapper

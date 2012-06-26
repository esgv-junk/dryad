from functools import wraps

def read_only_property(field_name):
    return property(lambda self: getattr(self, field_name))

def arg_decorator(decorator):
    return lambda func: lambda arg: func(decorator(arg))

def cache(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        key = (args, kwds)
        if key not in wrapper.cache:
            wrapper.cache[key] = f(*args, **kwds)
        return wrapper.cache[key]

    return wrapper




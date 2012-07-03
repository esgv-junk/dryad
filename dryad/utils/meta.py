from collections import Iterable
from functools import wraps, partial as _partial

def read_only_property(field_name):
    return property(lambda self: getattr(self, field_name))

# TOOLS FOR CONTSTRUCTING DECORATORS

def arg_decorator(decorator):
    return lambda f: wraps(f)(lambda arg: f(decorator(arg)))

def partial_(decorator):
    pass

# DECORATORS

def vectorize(f):
    @wraps(f)
    def wrapper(arg):
        if isinstance(arg, Iterable) and not isinstance(arg, basestring):
            return [f(_) for _ in arg]
        return f(arg)

    return wrapper

class Cache(dict):
    def pop(self, *args):
        return dict.pop(self, args, None)

def cache(f):
    @wraps(f)
    def wrapper(*args):
        key = args
        if key not in wrapper.cache:
            wrapper.cache[key] = f(*args)
        return wrapper.cache[key]

    wrapper.cache = Cache()
    return wrapper


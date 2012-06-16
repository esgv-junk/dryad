def read_only_property(field_name):
    return property(lambda self: getattr(self, field_name))

def arg_decorator(decorator):
    return lambda func: lambda arg: func(decorator(arg))

"""Напишите декоратор, который бы проверял тип параметров функции, конвертировал их
если надо и складывал"""

def _type(name):
    t = getattr(__builtins__, name)
    if isinstance(t, type):
        return t
    raise ValueError(name)


def typed(type):
    def decorator(f):
        def wrapper(*args, **kwargs):
            tp = _type(type)
            args = map(tp, args)
            kwargs = {k: tp(v) for k, v in kwargs.items()}
            return f(*args, **kwargs)
        return wrapper
    return decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c

@typed(type='float')
def add_three_symbols(a, b, c):
    return a + b + c

print(add_three_symbols(5,6,7))
print(add_three_symbols("3", 5,0))
print(add_three_symbols(0.1, 0.2, 0.4))
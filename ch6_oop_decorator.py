# from functools import wraps

# def func(arg1, arg2):
#     # arg1, arg2 : fake params for exercise
#     print("hi")

# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         func(*args, **kwargs)
#     return wrapper

# f = decorator(func)

class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = (list(range(0, len(data), 2)) +
                            list(range(1, len(data), 2)))

    def __iter__(self):
        return self

    def next(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration

oddeven = OddEven('ThIsIsCoOl!')
print(c for c in oddeven) # generator!
print(''.join(c for c in oddeven)) # TIICO!hssol

# oddeven = OddEven('HoLa') # or manually...
# it = iter(oddeven) # this calls oddeven.__iter__ internally

# print(next(it)) # H
# print(next(it)) # L
# print(next(it)) # o
# print(next(it)) # a
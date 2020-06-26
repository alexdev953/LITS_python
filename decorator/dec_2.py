def dec_argument(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
    return wrapper

@dec_argument
def func_with_argument(a, b):
    pass

func_with_argument('a','b')
from functools import partial
def print_r(a, b):
    print("a", a)
    print("b", b)

# print_r(1, 2)

func = partial(print_r, 3, 5)

func()
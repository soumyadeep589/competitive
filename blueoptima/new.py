from functools import partial

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        
        def print_i(a):
            print(a)
        ptr = partial(print_i, i)
        flist.append(ptr)

    return flist

functions = make_functions()
for f in functions:
    f()
    # [print_i(), print_i(), print_i()]
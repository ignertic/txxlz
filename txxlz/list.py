from itertools import chain

def flatten(lst):
    #return flattened list
    return chain.from_iterable(lst)

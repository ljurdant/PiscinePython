from functools import reduce

def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    try:
        iter(iterable)
    except:
        raise TypeError("ft_reduce() arg 2 must support iteration") from None
    try:
        iter(iterable)
        function_to_apply(iterable[0], iterable[0])
    except IndexError as te:
        raise TypeError("ft_reduce() of empty sequence with no initial value") from None
    except TypeError:
        return None

    m = iterable[0]
    for i in range(1, len(iterable)):
        m = function_to_apply(m, iterable[i])
    return m

# red = ft_reduce(lambda u, v: u + v,  ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"])
# # red_noniter = ft_reduce(lambda u, v: u + v, 6)
# red_badfunction = ft_reduce(lambda u, v: u / v,  ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"])
# # red_empty = ft_reduce(lambda u, v: u + v, [])

# print(red)
# print(red_badfunction)
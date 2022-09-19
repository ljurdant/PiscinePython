def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """

    for i in iterable:
        yield function_to_apply(i)

x = [1, 2, 3, 4, 5]

mp = ft_map(lambda dum: dum + 1, x)
mp_err = ft_map(lambda dum: dum + 1, 3)

# mp_error = ft_map(lambda dum, o: dum + o, 3)

# mp_real = map(lambda dum, o: dum + o , x)

print(mp)
print(list(mp))
print(list(mp_err))
# print(mp_error)
# print(list(mp_error))
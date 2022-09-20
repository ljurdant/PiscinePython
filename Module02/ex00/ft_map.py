
def ft_map_generator(function_to_apply, iterable):
    for i in iterable:
        yield function_to_apply(i)
    
def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    iter(iterable)
    try:
        function_to_apply(iterable[0])
    except:
        return None
    return ft_map_generator(function_to_apply, iterable)

# x = [1, 2, 3, 4, 5]

# mp = ft_map(lambda dum: dum + 1, x)
# # mp_noniter = ft_map(lambda dum: dum + 1, 5)
# mp_badfunction = ft_map(lambda dum: dum / 4, "hello")

# print(mp)
# print(mp_badfunction)
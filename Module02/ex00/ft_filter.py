def ft_filter_generator(function_to_apply, iterable):
    for i in iterable:
        if function_to_apply(i):
            yield i

def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        An iterable.
        None if the iterable can not be used by the function.
    """
    iter(iterable)
    try:
        if len(iterable):
            function_to_apply(iterable[0])
    except:
        return None
    return (ft_filter_generator(function_to_apply, iterable))

# x = [1, 2, 3, 4, 5]
# fltr = ft_filter(lambda dum: not (dum % 2), [])
# # fltr_noniter = ft_filter(lambda dum: dum + 1, 5)
# fltr_badfunction = ft_filter(lambda dum: dum / 4, "filter")

# print(list(fltr))
# print(fltr_badfunction)


def addition(*args):
    """function sums all arguments and returns value"""
    # args_type = [type(arg) for arg in args]
    args_type = list(map(lambda x:type(x), args))

    if str not in args_type:
        total = 0
        for arg in args:
           total += arg
        return total
    else:
        raise TypeError("parameters CANT be type of String")
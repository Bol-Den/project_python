

def addition(*args):
    """function sums all arguments and returns value"""
    try:
        total = 0
        for arg in args:
           total += arg
        return total
    except:
        return "parameters cant be type of String"

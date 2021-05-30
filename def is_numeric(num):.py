def is_numeric(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"
print(is_numeric(4))
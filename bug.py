def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a # ZeroDivisionError
    else:
        return a / b # Potential ZeroDivisionError if b is 0

result = function_with_uncommon_error(0, 5)
print(result)
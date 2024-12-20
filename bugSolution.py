def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            return b / a
        else:
            return a / b
    except ZeroDivisionError:
        return float('inf')  # Or handle it appropriately

result = function_with_uncommon_error_solution(0,5)
print(result)

result2 = function_with_uncommon_error_solution(5,0)
print(result2)
def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        res = function(int_list)
        results[function.__name__] = res
    return results

print(apply_all_func([-8, 20.825, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 0, 15, 9], all, any))











def calculate_structure_sum(*value):
    res = 0
    for i in value:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):
            res += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            res += calculate_structure_sum(*i.items())
        elif isinstance(i, int):
            res += i
        elif isinstance(i, str):
            res += len(i)
    return res

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
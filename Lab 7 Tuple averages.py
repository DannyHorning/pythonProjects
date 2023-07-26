random_tuple = (4, 5, 4, 3, 9, 12, 19, 14, 12, 6, 9)
this_is_also_a_tuple = (45, 65, 23, 10, 92, 56)
a_third_tuple = (12, 43, 15, 89, 9, 2, 18)


def get_tuple_average(tuple):
    total = 0
    count = len(tuple)
    for number in tuple:
        total += number
        avg = total / count
    return avg


print(f'{get_tuple_average(random_tuple):.2f}')
print(f'{get_tuple_average(this_is_also_a_tuple):.2f}')
print(f'{get_tuple_average(a_third_tuple):.2f}')
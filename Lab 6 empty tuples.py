tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
set_of_tuples = set(tuples)
blanks = {()}
new_set = set_of_tuples.difference(blanks)
updated_tuples = list(new_set)
print(updated_tuples)
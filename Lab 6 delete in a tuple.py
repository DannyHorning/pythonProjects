tuples = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for empty in tuples:
    if len(empty) == 0:
        tuples.remove(empty)
print(tuples)
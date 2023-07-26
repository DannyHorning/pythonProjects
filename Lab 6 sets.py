ITS_set = {'CMPH-209', 'COMM-238', 'CPNT-219', 'CPRG-216', 'MATH-237', 'CPNT-224', 'CPRG-217', 'CPSY-204', 'CPSY-206', 'PHIL-241'}
SD_set = {'CPRG-213', 'COMM-238', 'CPNT-217', 'CPRG-216', 'MATH-237', 'CPRG-211', 'CPRG-250', 'CPSY-200', 'CPSY-202', 'PHIL-241'}

combined = ITS_set.intersection(SD_set)

ITS_unique = ITS_set.difference(combined)

SD_unique = SD_set.difference(combined)

print("Common 1st Year Courses:")
for common in combined:
    print(common)
print("ITS-only Courses:")
for its in ITS_unique:
    print(its)
print("SD-only courses:")
for sd in SD_unique:
    print(sd)
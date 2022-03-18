
#reade file 1

from unittest import result


with open("DAY26/file1.txt") as data:
    first_list = data.readlines()

with open("DAY26/file2.txt") as data:
    second_list = data.readlines()

results = [int(n) for n in set(first_list).intersection(set(second_list))]
print(results)
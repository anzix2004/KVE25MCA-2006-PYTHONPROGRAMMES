# Program to sort dictionary keys
my_dict = {'c': 3, 'a': 1, 'b': 2}
asc = dict(sorted(my_dict.items()))

print("ascending Order:", asc)
desc = dict(sorted(my_dict.items(), reverse=True))

print("Descending Order:", desc)
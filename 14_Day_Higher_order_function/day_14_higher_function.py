# simple function
def make_uppercase(name):
    return name.upper()

names = ["azka", "ade", "parhan"]

upper_names = list(map(make_uppercase, names))

print(upper_names)
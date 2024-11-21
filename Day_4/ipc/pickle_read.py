from pickle import load

with open("pickled.dat") as src:
    a = load(src)
    b = load(src)
    c = load(src)
    d = load(src)


print a
print b
print c
print d

c.drive()

from pickle import dumps, dump
from car import Car

a = [10, 20, 30, 40]
b = {
    "name" : "Sam",
    "city" : "Mumbai"
}

c = Car("Toyota")
d = "this is a test string"

print dumps(a)
print "-" * 40
print dumps(b)
print "-" * 40
print dumps(c)
print "-" * 40
print dumps(d)
print "-" * 40

with open("pickled.dat", "w") as out:
    dump(a, out)
    dump(b, out)
    dump(c, out)
    dump(d, out)



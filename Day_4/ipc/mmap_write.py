from mmap import *

with open("/dev/shm/a.dat", "w+") as f:
    f.truncate(100)
    m = mmap(f.fileno(), 100, MAP_SHARED, PROT_READ | PROT_WRITE)
    raw_input("File opened.")
    m.write("This is a test string")
    raw_input("Wrote some data")

print "Done"


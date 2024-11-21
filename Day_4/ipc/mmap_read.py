from mmap import *

with open("/dev/shm/a.dat", "r+") as f:
    m = mmap(f.fileno(), 100, MAP_SHARED, PROT_READ | PROT_WRITE)
    raw_input("File opened.")
    print m.readline()

print "Done"


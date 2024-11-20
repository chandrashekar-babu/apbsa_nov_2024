a = [100, 200, 300]

def testfn():
    print("In testfn: a =", a)
    a[0] = [1111, 200, 300] # a.__setitem__(0, [1111, 200, 300])
   

if __name__ == '__main__':
    print("In main program: a =", a)
    testfn()
    print("In main program: a now is", a)

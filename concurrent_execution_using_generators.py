from time import sleep

def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        yield
        sleep(1)
        

def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        yield
        sleep(1)

if __name__ == '__main__':
    g1 = foo()
    g2 = bar()
    print(g1, g2)
    for _ in zip(g1, g2):
        pass

    
        
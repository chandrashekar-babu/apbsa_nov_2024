from time import sleep

def foo():
    for i in range(10):
        print(f"foo: counting {i}")
        sleep(1)

def bar():
    for i in range(10):
        print(f"bar: counting {i}")
        sleep(1)

if __name__ == '__main__':
    foo()
    bar()
    
        
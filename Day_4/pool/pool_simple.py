from multiprocessing import Pool



if __name__ == '__main__':
    def foo(x, y):
        print("foo called: x = {}, y = {}".format(x,y))
        return x + y

    def bar(x, y):
        print("bar called: x = {}, y = {}".format(x,y))
        return x * y

    def test(x):
        print("test called: x = {}".format(x))
        return x ** x

    def square(x): return x*x

    with Pool(10) as pool:
        foo_result = pool.apply_async(foo, args=(10, 20))
        bar_result = pool.apply_async(bar, args=("Hello", 10))
        test_result = pool.apply_async(test, args=(100,))

        print(foo_result.get(), bar_result.get(), test_result.get())

        result = pool.map(square, range(100))
        print("result =", result)




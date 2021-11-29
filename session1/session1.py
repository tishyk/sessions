d = {"key": "mit",
     "name": "MIT License",
     "spdx_id": "MIT",
     "url": "https://api.github.com/licenses/mit",
     "node_id": "MDc6TGljZW5zZTEz",
     'y': 1000}



dl = list(d.keys())


def func4(x, y=[], *args, **kwargs):
    print(x, y, args, len(args), kwargs)


def check_license(license, expected_keys=84, **kwargs):
    """Check a github api license data correspond to expected"""
    expected_license = {"key": "mit",
                        "name": "MIT License",
                        "spdx_id": "MIT",
                        "url": "https://api.github.com/licenses/mit",
                        "node_id": "MDc6TGljZW5zZTEz"}


def func3(*args):
    print(args)  # --> tuple()
    # print(args)  # --> (10,)
    # print(args)  # --> (10, 20, 0)
    for i in args:
        print(i)


def func2(**kwargs):
    print(kwargs)  # --> {}
    # print(args)  # --> {key:value}
    # print(args)  # --> (10, 20, 0)
    for i in kwargs:
        print(i)


if __name__ == "__main__":
    print(__file__, __name__)   # C:\Projects\PythonOct2021\session1\session1.py __main__
    func3()
    func3(10)
    func3(10, 20, 0)
    func3(dl)  # ("key","name"... )
    func2()
    func2(**d)  # func2(key="mit",name="MIT License",...)

    func4(0, **d)
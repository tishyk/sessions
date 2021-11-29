# class A:
#     def __init__(self):
#         print("class A")
#
#     def hello(self):
#         print(f"Hello from {self.__class__.__name__}", 'A')
#
#
# class B(A):
#     def __init__(self):
#         print("class B")
#
#     def hello(self):
#         print(f"Hello from {self.__class__.__name__}", "B")
#
#
# class C():
#     def __init__(self):
#         print("class C")
#
#
# class D(C):
#     def __init__(self):
#         print("class D")
#
#
# class E(D, B):
#     def __init__(self):
#         print("class E")
#         super().__init__()   # D
#         super(D, self).__init__()   # D <- C
#         super(C, self).__init__()   # C <- B
#         super(B, self).__init__()   # B <- A
#
#
#     def hello(self):
#         print(f"Hello from {self.__class__.__name__}", "E")
#
#
# e = E()

#
# class Q(E,D):
#     pass
#
# # class W(B,D,E):
# #     pass
# #Traceback (most recent call last):
# #   File "<input>", line 1, in <module>
# # TypeError: Cannot create a consistent method resolution
# # order (MRO) for bases B, E, D
#
# class Y:
#     pass
#
# class W(Y, E, A):
#     def old_hello(self):
#         pass
#
#     def hello(self):
#         print("W")
#
#     def __call__(wd):
#         print(wd)
#
# print(W.__mro__)
# # A.__subclasses__()
# w = W()
# w
# pass
#
#

class A:
    title = "Book A"
    def __init__(self):
        print("class A")


class B(A):
    def __init__(self):
        print("class B")

    def hello(self):
        print(f"Hello from {self.__class__.__name__}", "B")


class C(A):
    def __init__(self):
        print("class C")

class M:
    def show_title(self):
        print(self.title)

class B1(B, M):
    pass

class C1(C, M):
    pass


b1 = B1()
c1 = C1()

b1.show_title()
c1.show_title()
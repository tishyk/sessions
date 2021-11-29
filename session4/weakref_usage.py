import sys
import gc
from weakref import getweakrefcount, ref, proxy, WeakValueDictionary, WeakKeyDictionary

"""
Problem

Not all objects can be weakly referenced; those objects which can include class instances,
 functions written in Python (but not in C), instance methods, sets, frozensets, some file objects,
  generators, type objects, sockets, arrays, deques, regular expression pattern objects, and code objects.
  
Several built-in types such as LIST and DICT do not directly support weak references
 but can add support through subclassing:

class Dict(dict):
    pass

obj = Dict(red=1, green=2, blue=3)   # this object is weak referencable
"""


class Book():
    def __init__(self, name: str):
        self.name = name
        self.content = "Speckled Chicken ..."
        self.address: int

    @staticmethod
    def destroy_callback(wr_book):
        # print(wr_book) ---> ReferenceError: weakly-referenced object no longer exists
        print("Callback function for destroyed object. This will work when the book object is deleted")

    @staticmethod
    def destroy_callback_proxy(wr_book):
        # print(wr_book) --> ReferenceError: weakly-referenced object no longer exists
        print(f"Callback function for destroyed object. This will work when the book object is deleted")

    @staticmethod
    def cleanup(wr_book):
        wr_book = 10
        print(1 , wr_book) #--> ReferenceError: weakly-referenced object no longer exists
        print("Clean up")


class Library:
    def __init__(self, name: str):
        self.name = name
        self.catalog: dict[book.name, book.address] = {}
        self.shelves = {}
        self.current_shelf: dict['address', id, 'books', list]
        self.add_shelf('1fl32r')

    def add_shelf(self, name: str):
        if self.shelves.setdefault(name,
                                   {'address': id(name), 'books': []}):
            print("New shelf created")
        self.current_shelf = self.shelves[name]

    def add_book(self, book: Book) -> int:
        # library.show_references(book)
        self.current_shelf['books'].append(book)
        book.address = self.current_shelf.get('address')
        self.catalog[book.name] = book.address
        print(f'Book "{book.name}" added to {book.address}')
        return book.address

    @staticmethod
    def show_references(book_obj):
        "Print count of refs to book_obj and count of weak refs"
        print(f"strong refs: {sys.getrefcount(book_obj)} | weak refs: {getweakrefcount(book_obj)}")



# book = Book('Fairy tales')
# library = Library("Quiet place")
#
# # Count initial book references
# library.show_references(book)
#
# # Count book references after book added into dict or list objects
# library.add_book(book)
# library.show_references(book)
# print(library.shelves)
#
# # Create weak reference. Add callback for book object reference delete step
# book_weak_reference = ref(book, book.destroy_callback)
# # book_weak_reference() to get book value
# library.show_references(book)
#
# # del book
#
# library.show_references(book)  # will be failed with "NameError: name 'book' is not defined"
# #
# # The original object can be retrieved by CALLING the reference object if the referent is still alive;
# # if the referent is no longer alive, calling the reference object will cause None to be returned.
#
# print(library.shelves)
#
# # Create proxy weak reference. Add callback for book object reference delete step
book_proxy = proxy(book, book.destroy_callback_proxy)
#
# print(book_proxy.address)
#
# library.show_references(book)
# # del library
# # del book
# # gc.collect()
#
# # Create weak books storage
# #
books_as_values = WeakValueDictionary()
books_as_values[book.name] = book  # will delete key if value was deleted

books_as_keys = WeakKeyDictionary()
books_as_keys[book] = book.address  # will delete value if key was deleted
#
# # del library.shelves['1fl32r']['books']
# del library
#
# print(f"The number of unreachable objects is {gc.collect()}")
# Library.show_references(book)
#
# del book
#
#
# for wv in weak_initial_values:
#     if wv:
#         print(wv.idx)
# real_initial_values.pop(-1)

#
#
# real_books = [Book(i) for i in range(1000)]
# books = WeakValueDictionary()
# books.update({book.idx:book for book in real_books})
#
# for book in books:
#     print("Book id:", book, books.get(book).name)

class WRLib(Library):
    def __init__(self, name):
        super().__init__(name)

    def add_book(self, bookref: ref) -> int:
        self.current_shelf['books'].append(bookref)
        bookref().address = self.current_shelf.get('address')
        self.catalog[bookref().name] = bookref().address
        print(f'Book "{bookref().name}" added to {bookref().address}')
        return bookref().address


library = WRLib("Quiet place with weak references")
book = Book('Fairy tales for quite place')

library.show_references(book)
wr_book = ref(book, Book.cleanup)
library.show_references(book)

library.add_book(wr_book)
library.show_references(book)

del book
print(f"The number of unreachable objects is {gc.collect()}")
print(library.shelves)

# print(library.shelves,
#       library.catalog,
#       library.current_shelf['books'],
#       sep='\n')

# New shelf created
# strong refs: 5 | weak refs: 0
# strong refs: 5 | weak refs: 1
# Book "Fairy tales for quite place" added to 2859246975984
# strong refs: 5 | weak refs: 1

# but after book del for proxy refs:
# library.shelves
# {'1fl32r': {'address': 2859246975984, 'books': [<weakproxy at 0x00000299B86B80E0 to NoneType at 0x00007FFA3CCF3CD8>]}}
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.2\plugins\python-ce\helpers\pydev\_pydevd_bundle\pydevd_xml.py", line 255, in frame_vars_to_xml
#     eval_full_val = should_evaluate_full_value(v)
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.2\plugins\python-ce\helpers\pydev\_pydevd_bundle\pydevd_utils.py", line 590, in should_evaluate_full_value
#     or ((is_builtin(type(val)) or is_numpy(type(val))) and not isinstance(val, (list, tuple, dict, set, frozenset))) \
# ReferenceError: weakly-referenced object no longer exists
# Unexpected error, recovered safely.
# library.catalog
# {'Fairy tales for quite place': 2859246975984}
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.2\plugins\python-ce\helpers\pydev\_pydevd_bundle\pydevd_xml.py", line 255, in frame_vars_to_xml
#     eval_full_val = should_evaluate_full_value(v)
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2021.1.2\plugins\python-ce\helpers\pydev\_pydevd_bundle\pydevd_utils.py", line 590, in should_evaluate_full_value
#     or ((is_builtin(type(val)) or is_numpy(type(val))) and not isinstance(val, (list, tuple, dict, set, frozenset))) \
# ReferenceError: weakly-referenced object no longer exists
# Unexpected error, recovered safely.
x = 0


class Title:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        # instance: is the instance being manipulated
        print("Get name:", self.name)
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < 3:
            raise TypeError("Expected type 'str' with len more than 3 symbols")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = ''
        print("Delete:", self.name)

class Book:
    title = Title('title')

    def __init__(self, title):
        self.title = title

book = Book("Pic")
print(book.title)
del book.title
"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface for operations that create abstract product
    objects.
    """

    @abc.abstractmethod
    def chair(self):
        pass

    @abc.abstractmethod
    def sofa(self):
        pass


class ArtDeco(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def chair(self):
        return ArtDecoChair()

    def sofa(self):
        return ArtDecoSofa()


class Victorian(AbstractFactory):
    """
    Implement the operations to create concrete product objects.
    """

    def chair(self):
        return VictorianChair()

    def sofa(self):
        return VictorianSofa()



class Chair(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def seat(self):
        pass


class ArtDecoChair(Chair):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def seat(self):
        pass


class VictorianChair(Chair):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def seat(self):
        pass


class Sofa(metaclass=abc.ABCMeta):
    """
    Declare an interface for a type of product object.
    """

    @abc.abstractmethod
    def clean(self):
        pass


class ArtDecoSofa(Sofa):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def clean(self):
        pass


class VictorianSofa(Sofa):
    """
    Define a product object to be created by the corresponding concrete
    factory.
    Implement the AbstractProduct interface.
    """

    def clean(self):
        pass


def main():
    for factory in (ArtDeco(), Victorian()):
        product_a = factory.chair()
        product_b = factory.sofa()
        product_a.seat()
        product_b.clean()


if __name__ == "__main__":
    main()

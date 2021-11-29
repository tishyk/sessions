"""
Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.
"""

import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Subject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        # ...
        self._real_subject.request()
        # ...


class RealSubject(Subject):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        pass


def main():
    proxy = Proxy()
    proxy.request()


if __name__ == "__main__":
    main()

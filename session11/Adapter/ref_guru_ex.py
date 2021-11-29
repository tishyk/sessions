#https://refactoring.guru/ru/design-patterns/adapter/python/example#lang-features

class Target():
    """
    Целевой класс объявляет интерфейс, с которым может работать клиентский код.
    """

    def request(self) -> str:
        raise RuntimeError('d')
        return "Target: The default target's behavior."


class Adaptee:
    """
    Адаптируемый класс содержит некоторое полезное поведение, но его интерфейс
    несовместим с существующим клиентским кодом. Адаптируемый класс нуждается в
    некоторой доработке, прежде чем клиентский код сможет его использовать.
    """

    def specific_request(self) -> str:
        raise RuntimeError('d')
        return ".eetpadA eht fo roivaheb laicepS"

    def specific_request2(self) -> str:
        return bytes(".eetpadA eht fo roivaheb laicepS", 'utf-8')



class TargetJSON(Target):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        #raise RuntimeError('AdapterJson failed')
        return f"AdapterJson: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"

class TargetYAML(TargetJSON):
    """
    Адаптер делает интерфейс Адаптируемого класса совместимым с целевым
    интерфейсом.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter YAML: (TRANSLATED) {self.adaptee.specific_request2().decode('ascii')[::-1]}"


# --------------------------------------------------------------


def client_code(target: Target) -> None:
    """
    Клиентский код поддерживает все классы, использующие интерфейс Target.
    """


    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    # client_code(target)
    #print("\n")

    adaptee = Adaptee()
    #print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    #print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    #print("Client: But I can work with it via the Adapter:")
    target = Target()
    adapter_json = TargetJSON(adaptee)
    adapter_yaml = TargetYAML(adaptee)

    try:
        data = client_code(target)
    except RuntimeError:
        try:
            data = client_code(adapter_json)
        except RuntimeError:
            data = client_code(adapter_yaml)

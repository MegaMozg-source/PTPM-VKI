import abc

class UserInterface(abc.ABC):
    @abc.abstractmethod
    def get_input(self) -> tuple:
        pass

class ConsoleUserInterface(UserInterface):
    def get_input(self) -> tuple:
        a = input("Введите сторону A: ")
        b = input("Введите сторону B: ")
        c = input("Введите сторону C: ")
        return a, b, c
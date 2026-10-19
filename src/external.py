import abc

class ExternalService(abc.ABC):
    @abc.abstractmethod
    def send(self, message: str):
        pass

class MockEmailService(ExternalService):
    def send(self, message: str):
        print(f"[ИМИТАЦИЯ ОТПРАВКИ] Отправлено: {message}")
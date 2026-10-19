from src.calculator import TriangleCalculator
from src.database import Database
from src.ui import UserInterface
from src.external import ExternalService


class Controller:
    def __init__(self, db: Database, ui: UserInterface, ext_service: ExternalService):
        self.db = db
        self.ui = ui
        self.ext_service = ext_service

    def run(self):
        a, b, c = self.ui.get_input()
        record = self.db.get_record(a, b, c)

        if record:
            kind, error = record
            result_msg = f"Из БД: Тип: {kind}. Ошибка: {error if error else 'нет'}"
        else:
            kind, error, coords = TriangleCalculator.get_triangle_info(a, b, c)
            self.db.add_record(a, b, c, kind, error)
            result_msg = f"Вычислено: Тип: {kind}. Ошибка: {error if error else 'нет'}"

        self.ext_service.send(result_msg)
        return result_msg
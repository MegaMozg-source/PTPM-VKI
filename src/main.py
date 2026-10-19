from src.database import Database
from src.ui import ConsoleUserInterface
from src.external import MockEmailService
from src.controller import Controller

if __name__ == "__main__":
    db = Database("triangles.db")
    ui = ConsoleUserInterface()
    ext = MockEmailService()

    app = Controller(db, ui, ext)
    app.run()
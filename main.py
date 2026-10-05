import logging
import os
import sys

import triangle


LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")


def main():
    os.makedirs(LOG_DIR, exist_ok=True)


    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s | [%(levelname)-7s] | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(os.path.join(LOG_DIR, "file_txt.log"), encoding="utf-8"),
        ],
    )
    logging.info("Логгер сконфигурирован, приложение запущено")


    while True:
        print("\n--- Новый треугольник (введите 'q' для выхода) ---")

        str_a = input("Сторона A = ").strip()
        if str_a.lower() == "q":
            logging.info("Пользователь завершил работу")
            print("Выход.")
            break

        str_b = input("Сторона B = ").strip()
        if str_b.lower() == "q":
            logging.info("Пользователь завершил работу")
            print("Выход.")
            break

        str_c = input("Сторона C = ").strip()
        if str_c.lower() == "q":
            logging.info("Пользователь завершил работу")
            print("Выход.")
            break

        kind, coords = triangle.get_triangle_info(str_a, str_b, str_c)
        print("Тип треугольника:", kind)
        print("Координаты вершин:", coords)

if __name__ == "__main__":
    main()
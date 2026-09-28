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


    str_a = input("Сторона A = ").strip()
    str_b = input("Сторона B = ").strip()
    str_c = input("Сторона C = ").strip()


    kind, coords = triangle.get_triangle_info(str_a, str_b, str_c)
    print("Тип треугольника:", kind)
    print("Координаты вершин:", coords)


if __name__ == "__main__":
    main()

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def edge(city, **place):
    print(f"Край: {city}")
    for place, name in place.items():
        sorted(place)
        print(f"{place}: {name}")


if __name__ == "__main__":
    edge(
        "Ставропольский",
        Ставрополь="Крепостная гора", Пятигорск="Памятник на месте дуэли М.Ю.Лермонтова",
        Кисловодск="Кисловодский парк", Невинномысск="Бульвар Мира",
        Ессентуки="Питьевая галерея «Пятитысячник»")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def min_sum(*args):
    if args:
        min_index = args.index(min(args))
        summa = 0
        for i in range(min_index + 1, len(args)):
            summa += args[i]
        return summa
    else:
        return None


if __name__ == '__main__':
    print(f"Сумма равна: {min_sum(5, 2, 3, 1, 5, 3, 4, 6)}")


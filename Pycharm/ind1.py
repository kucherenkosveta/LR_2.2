#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = int(input("Value of N? "))
    if 20 >= N >= 0:
        if N == 1:
            print(f"Мы успешно сдали 1 экзамен")
        elif N == 2 or N == 3 or N == 4:
            print(f"Мы успешно сдали {N} экзамена")
        else:
            print(f"Мы успешно сдали {N} экзаменов")
    else:
        print("Ошибка!")



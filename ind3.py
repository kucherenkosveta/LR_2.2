#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for x in range(10, 100, 1):
        sum = x // 10 + x % 10
        if x == sum + sum**2:
            print(f"Полученные числа: {x}")
        
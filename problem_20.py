#!/usr/bin/python
# title          :problem_20.py
# description    :Project Euler - Problem 20 (https://projecteuler.net/)
# author         :Gabriel Ionescu
# date           :2017/09/27
# version        :1.0
# notes          :
# python_version :3.6.1
# ========================================================================

"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

from math import factorial

def main(x):
    nr = str(factorial(x))
    sum = 0
    for elem in nr:
        sum += int(elem)
    print(sum)

if __name__ == '__main__':
    main(100)
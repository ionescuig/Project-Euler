#!/usr/bin/python
# title          :problem_21.py
# description    :Project Euler - Problem 21 (https://projecteuler.net/)
# author         :Gabriel Ionescu
# date           :2017/09/27
# version        :1.0
# notes          :the list is note made
# python_version :3.6.1
# ========================================================================

"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of
220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def main():
    d = {}
    suma = 0
    for i in range(2,10001):
        d[i] = 0
    for key, val in d.items():
        for i in range(1,int(key/2)+1):
            if key % i == 0:
                d[key] += i
                
    for key1, val1 in d.items():
        for key2, val2 in d.items():
            if key2 == val1 and key1 == val2 and key1 != key2:
                print(key1, val1, "\t", key2, val2)
                suma += key1

    print(suma)
    

if __name__ == '__main__':
    main()

#!/usr/bin/python
# title          :problem_22.py
# description    :Project Euler - Problem 22 (https://projecteuler.net/)
# author         :Gabriel Ionescu
# date           :2017/10/11
# version        :1.0
# notes          :
# python_version :3.6.1
# ========================================================================


"""
Using problem_22_names.txt, a 46K text file
containing over five-thousand first names,
begin by sorting it into alphabetical order.

Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def main(file):

    # copy our names from file to a list
    lista = []
    with open(file) as f:
        line = f.readlines()

    lista = line[0].split(',')
    for elem in range(len(lista)):
        lista[elem] = lista[elem].replace('"','')

    lista.sort()

    # make the total of the score for each name
    total = 0
    for index in range(len(lista)):
        score = 0
        for char in lista[index]:
            score += ord(char) - 64
        score = score * (index + 1)
        total += score

    # return our total
    return(total)


if __name__ == '__main__':
    print(main('problem_22_names.txt'))

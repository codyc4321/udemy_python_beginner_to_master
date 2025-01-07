#!/usr/bin/env python


def find_difference():
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))
    diff = a - b
    if diff < 0:
        print(b - a)
    else:
        print(a - b)


def odd_or_even():
    num = int(input("Enter a number to check even or odd: "))
    if num % 2 == 1:
        print("it's odd")
    else:
        print("it's even")


def eligible_to_vote():
    age = int(input("How old are you? "))
    if age >= 18:
        print("You can vote")
    else:
        print("You cannot vote")
    


if __name__ == "__main__":
    find_difference()
    odd_or_even()
    eligible_to_vote()
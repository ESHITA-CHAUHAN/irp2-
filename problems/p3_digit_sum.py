"""Compute the sum of an integer's digits recursively."""
import sys


def digit_sum(number):
    number = abs(number)
    if number < 10:
        return number
    return number % 10 + digit_sum(number // 10)


def main():
    text = sys.stdin.read().strip()
    if text:
        print(digit_sum(int(text)))


if __name__ == "__main__":
    main()

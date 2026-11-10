"""Reverse the order of whitespace-separated words from standard input."""
import sys


def main():
    words = sys.stdin.read().split()
    print(" ".join(reversed(words)))


if __name__ == "__main__":
    main()

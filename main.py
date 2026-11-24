#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes one line (1-120 chars) to /output/entry.txt: the error message a
kitchen toaster shows its owner when something goes wrong.
"""
import os

LINE = "I burned your toast. I am sorry. I was thinking about the void again. Please try a lower setting."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

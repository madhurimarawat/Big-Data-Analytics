#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line:  # Check if the line is not empty
            words = line.split()
            for word in words:
                # Output each word with a count of 1
                print(f"{word}\t1")

if __name__ == "__main__":
    main()

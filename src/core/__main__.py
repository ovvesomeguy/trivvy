#!/usr/bin/python3.6

"""
        The main entry point.
"""

import sys

def main():
        try:
                from entry import main
                sys.exit(main())
        except KeyboardInterrupt:
                sys.exit(0)

if __name__ == "__main__":
        main()
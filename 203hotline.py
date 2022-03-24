#!/usr/bin/env python3

from curses.ascii import isdigit
import sys

def print_helper():
    print ("USAGE")
    print ("\t./203hotline [n k | d]")
    print ("\nDESCRIPTION")
    print ("\tn \tn value for the computation of C(n, k)")
    print ("\tk \tk value for the computation of C(n, k)")
    print ("\td \taverage duration of calls (in seconds)")

def error_handling(argv):
    if (len(argv) == 2):
        if (argv[1] == "-h"):
            print_helper()
            sys.exit(0)
        elif (argv[1].isdigit() == False):
            sys.exit(84)
    if (len(argv) != 2 and len(argv) != 3):
        sys.exit(84)
    if (argv[1].isdigit() == False or argv[2].isdigit() == False):
        sys.exit(84)
    if (int(argv[1]) <= 0 or int(argv[2]) <= 0):
        sys.exit(84)

def main(argv):
    error_handling(argv)
    print("test")
    exit (0)

main(sys.argv)

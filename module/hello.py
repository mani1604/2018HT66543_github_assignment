#!/usr/local/bin/python3.7

# =========================================================================================
#
# NAME:           hello.py
# DESCRIPTION:    Python module to print greetings
# AUTHOR:         Manish Sharma
# VERSION:        1.0
# CREATED:        Oct 16, 2019
#
# =========================================================================================

def greet(fname):
    print(f"Hello, {fname}")

fname = str(input("What's your name?: ").strip())
greet(fname)

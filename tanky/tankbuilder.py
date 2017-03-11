#!/usr/bin/env python
import os
import subprocess


if __name__ == '__main__:
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('cls', shell=True)

main()

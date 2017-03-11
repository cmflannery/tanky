#!/usr/bin/env python
import os
import subprocess
import core.structural


def main():
    print('main')
    return 0


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('cls', shell=True)
    main()

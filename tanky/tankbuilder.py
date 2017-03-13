#!/usr/bin/env python
import os
import subprocess
from openpyxl import load_workbook, Workbook
import core.structural as struct
import core.parameters as params
import core.io as io


def load_inputs():
    dirPath = os.path.dirname(__file__)
    inputPath = os.path.join(dirPath, 'input', 'input.xlsx')
    wb = load_workbook(filename=inputPath, read_only=True)

    return wb


def main():
    inputwb = load_inputs()  # function call; get input workbook(s)
    inputParams = io.InputPull(inputwb)

    print(inputParams.material)
    designframe = params.DesignParameters()
    designframe.prompt_sf()

    return 0


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('cls', shell=True)
    main()

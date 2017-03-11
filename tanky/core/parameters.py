#!/usr/bin/env python


class DesignParameters:
    """ DesignParameters: Stores design parameters taken from user prompts"""
    def init(self):
        return 0

    def prompt_sf(self, *arg):
        if len(arg) == 0:
            continue
        else:
            arg(1) = self.sfy
            arg(2) = self.sfu
        try:
            self.sfy = eval(input("Enter the Yield Factor of Safety: "))
            self.sfu = eval(input("Enter the Ultimate Factor of Safety: "))
        except NameError:
            print("Error: Values must be numbers.")

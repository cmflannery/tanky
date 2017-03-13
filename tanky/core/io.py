#!/usr/bin/env python


class InputPull:
    """ InputFile is a class that expects a workbook opened in read-only mode
    with openpyxl as an argument in the instance initiation call.
    All subsequent parsing actions are predefined based on expected
    input format """
    def __init__(self, *arg):
        self.wb = arg[0]
        self.inputSheet = self.wb['inputs']
        self.pull_title()
        self.pull_name()
        self.pull_prop()
        self.pull_flight()
        self.pull_mat()

    def pull_title(self):
        temp = self.inputSheet['C2']
        self.title = temp.value

    def pull_name(self):
        temp = self.inputSheet['C3']
        self.name = temp.value

    def pull_prop(self):
        """ pull propellant properties from input sheet and assign to class
        variables """
        propellants = self.inputSheet['C7:C12']
        a = propellants[0]
        self.oxidizer = propellants[0].value
        self.rho_oxidizer = propellants[1].value
        self.mdot_oxidizer = propellants[2].value
        self.fuel = propellants[3].value
        self.rho_fuel = propellants[4].value
        self.mdot_fuel = propellants[5].value

    def pull_flight(self):
        """ pull flight and performance properties from input sheet """
        flight = self.inputSheet['C16:C18']
        self.tb = flight[0].value  # nominal burn time (full thrust)

    def pull_mat(self):
        """ pull material properties from input sheet and assign to class
        variables """
        materials = self.inputSheet['C22:C23']
        self.material = materials[0].value
        self.sigmay = material[1].value
        self.sigmau = material[2].value

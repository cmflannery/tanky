# Welcome to tanky
[![Build status](https://travis-ci.org/cmflannery/tanky.svg?branch=master)](https://travis-ci.org/cmflannery/tanky)

[tanky](https://github.com/cmflannery/tanky) is an open source project that helps with the design of propellant tanks for liquid propellant rocket engines. Structural analysis and calculations are run with in the program.

### Release Notes
__Pre-Release__

Currently in pre-release. Code has not been validated or verified. __Use With Caution!!__

### Running tanky
Tanky requires python3. Future development will add functionality for python2.

#### Input File
input.xlsx is an excel input file. tanky looks in the input folder for a file named input.xlsx. Future versions may support multiple input files for one run. The output files are generated and stored in an output folder, named with a timestamp. The user should input values into the yellow highlited cells in the input file.

### Verification and Validation

#### Pylint
Regular pylint tests should be run to access code cleaniness.

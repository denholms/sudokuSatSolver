# sudokuSatSolver

## usage:
encoding.py -i <inputfile> -o <outputfile> -p <path to miniSAT executable relative to current directory> -n <number of rows> [encoding option]

Encoding options are restricted to '-e' for extended encoding.

Where the input file is the unsolved sudoku puzzle, the output file is the solved puzzle, and n is the number of rows or columns in the unsolved puzzle. For a 9x9 puzzle, n would be 9.

#Contents
encoding.py - The program itself

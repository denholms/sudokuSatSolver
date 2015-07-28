# sudokuSatSolver

## usage:
encoding.py -i <inputfile> -o <outputfile> -p <path to miniSAT executable relative to current directory> -n <number of rows> [encoding option]

Encoding options are restricted: '-e' for extended encoding.
-i : The input file (unsolved sudoku puzzle)
-o : The output file (solved sudoku puzzle)
-p : Path to the miniSAT executable, relative to the current working idrectory
-n : Number of rows / columns (for an 9x9 puzzle, n would be 9)

#Contents
encoding.py - The program itself

# sudokuSatSolver

## installation:
If the minisat is not already installed, 
  - unzip the minisat.tar.gz file provided using the command:  
    tar -zxf minisat.tar.gz
  - when running the program, use "minisat/core/minisat" as the path to the miniSAT executable (flag -p)
  
## usage:
encoding.py -i \<inputfile> -o \<outputfile> -p \<path to miniSAT executable relative to current directory> -n \<number of rows> [encoding option]

Encoding options are restricted: '-e' for extended encoding.  
-i : The input file (unsolved sudoku puzzle)  
-o : The output file (solved sudoku puzzle)  
-p : Path to the miniSAT executable, relative to the current working directory  
-n : Number of rows / columns (for an 9x9 puzzle, n would be 9)  

## contents:
encoding.py - The program itself
minisat.tar.gz - The compressed minisat

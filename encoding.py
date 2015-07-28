from subprocess import call
import sys, getopt, math, pprint

# encoding.py -i inputfile -o outputfile -n number

N = 0
C = 0

solution = []
puzzle = []

def read (file):
	string = ''
	f = open(file, "r")
	buff = f.readline().strip()
	while (buff != ''):
		string += buff
		buff = f.readline().strip()
	f.close()
	return string

def write ():
	f = open("mid.txt", "wb")
	global solution
	# count total number of clauses
	count = 0
	for cell in solution:
		count += 1

	f.write("p cnf " + str(getNumberOfVariables(N-1, N-1, N-1) + 1) + " " + str(count) + "\n")
	count = 0
	for cell in solution:
		for i in cell:
			f.write(str(i) + " ")
		f.write("0\n")
	f.close()


def parse(string):
	global puzzle
	string = string.replace("\n", "").replace("*", "0").replace(".", "0").replace("?", "0")
	counter = 0
	puzzle = [[0 for x in range (N)] for x in range (N)]
	if (len(string) != (N * N) or N < 1):
		print "invalid table"
		sys.exit(2)
	for row in range(N):
		for column in range(N):
			puzzle[row][column] = int(string[counter])
			counter += 1
	return puzzle

def getNumberOfVariables(value, row, column):
	return (N * N * row) + (N * column) + value

def eachCell():
	global solution
	for row in range (N):
		for column in range (N):
			clause = [];
			for value in range (1, N+1):
				clause.append(getNumberOfVariables(value, row, column))
			solution.append(clause)

def oncePerColumn():
	global solution
	for col in range (N):
		for value in range (1, N+1):
			for row in range (N-1):
				for nrow in range(row+1, N):
					solution.append([-getNumberOfVariables(value,row,col), -getNumberOfVariables(value, nrow, col)])

def oncePerRow():
	global solution
	for row in range (N):
		for value in range (1, N+1):
			for column in range (N-1):
				for ncol in range(column+1, N):
					solution.append([-getNumberOfVariables(value, row, column), -getNumberOfVariables(value, row, ncol)])

def oncePerGrid():
	global solution
	for value in range (1, N+1):
		for xbox in range(C):
			for ybox in range(C):
				for i in range(C):
					for j in range(C):
						for k in range(i+1, C):
							for l in range(C):
								solution.append([-getNumberOfVariables(value, (C * xbox) + i, (C * ybox) + j), -getNumberOfVariables(value, (C * xbox) + k, (C * ybox) + l)])

def addFromPuzzle():
	global puzzle
	global solution
	for row in range(N):
		for column in range(N):
			if(puzzle[row][column] > 0):
				solution.append([getNumberOfVariables(puzzle[row][column], row, column)])

#one number per cell
def checkCells():
	for row in range(N):
		for column in range(N):
			for i in range(1, N):
				for j in range(i+1, N+1):
					solution.append([-getNumberOfVariables(i, row, column), -getNumberOfVariables(j, row, column)])

#one number per row
def checkRows():
	for i in range(1, N+1):
		for column in range(N):
			vals = []
			for row in range(N):
				vals.append(getNumberOfVariables(i, row, column))
			solution.append(vals);

#one number per col
def checkCols():
	for i in range(1, N+1):
		for row in range(N):
			vals = []
			for column in range(N):
				vals.append(getNumberOfVariables(i, row, column))
			solution.append(vals);

#one number per grid
def checkGrids():
	for gridRow in range(C):
		for gridColumn in range(C):
			for i in range(1, N+1):
				vals = []
				for j in range(C):
					for k in range(C):
						vals.append(getNumberOfVariables(i, j + (C * gridRow), k + (C * gridColumn)))
				solution.append(vals)

def decodeSAT(output):
	print("\nSolved puzzle:\n")
	for i in range(N):
		for j in range(N):
			for k in range(1, N + 1):
				val = output[(N * N * i) + (N * j) + k - 1]
				if (int(val) > 0):
					sol = int(val) - (N * N * i) - (N * j)
					print(sol),
		print("\n")			

def printPuzzle(puzzle):
	print("\nUnsolved puzzle:\n")
	for i in range(N):
		for j in range(N):
			print(str(puzzle[i][j]).replace("0", ".")),
		print("\n")

def extendedEncoding():
	checkCells()
	checkRows()
	checkCols()
	checkGrids()

def minimalEncoding():
	addFromPuzzle()
	eachCell()
	oncePerColumn()
	oncePerRow()
	oncePerGrid()

def main(argv):
	inputfile = ''
	outputfile = ''
	extended = False
	global N
	global C

	try:
		opts, args = getopt.getopt(sys.argv[1:],"ehi:o:p:n:")
	except getopt.GetoptError:
		print 'usage: python encoding.py -i <inputfile> -o <outputfile> -n <number of rows> -p <path to minisat executable> -e (for extended encoding)'
		print getopt.GetoptError
		sys.exit(2)
	for option, arg in opts:
		if option in ("-i"):
			inputfile = arg
		elif option in ("-o"):
			outputfile = arg
		elif option in ("-n"):
			N = int(arg)
		elif option in ("-e"):
			extended = True
		elif option in ("-p"):
			minisat_path = arg
		elif option in ("-h"):
			print 'usage: python encoding.py -i <inputfile> -o <outputfile> -n <number of rows> -p <path to minisat executable> -e (for extended encoding)'
			sys.exit(2)
	if ((N is 0) or (inputfile is '') or (outputfile is '')):
		print 'usage: python encoding.py -i <inputfile> -o <outputfile> -n <number of rows> -p <path to minisat executable> -e (for extended encoding)'
		sys.exit(2)

	#try:
	global puzzle
	string = read(inputfile)
	C = int(math.sqrt(N))
	puzzle = parse(string)
	minimalEncoding()
	if(extended == True):
		extendedEncoding()
	write() #write to intermediate file for miniSAT reading

	call([minisat_path, "mid.txt", outputfile]) #assuming this is how the minisat accepts things.
	# ^^ we may need to adjust our write function to accomodate the minisat
	#except: #this is commented for now for development purposes
	#	print "failed read. for help use -h option"

	output = read(outputfile)
	if (output[0:3] == "SAT"):
		output_list = output[3:-1].split()
		printPuzzle(puzzle)
		decodeSAT(output_list)

if __name__ == "__main__":
	main(sys.argv[1:])

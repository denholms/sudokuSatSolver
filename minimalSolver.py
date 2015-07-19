from subprocess import call
import sys, getopt, math

# call(["minisat", "arg", "arg"])
# minimalSolver.py -i inputfile -o outputfile -n number

# Every row contains the number once
# Every column contains the number once
# Every number appears once in every grid

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
	f = open("mid.txt", "r+b")
	global solution
	for cell in solution:
		for i in cell:
			f.write(str(i) + " ")
		f.write("0\n")
	f.close()


def parse(string):
	string = string.replace("\n", "").replace("*", "0").replace(".", "0").replace("*", "0").replace("?", "0")
	counter = 0
	puzzle = [[0 for x in range (N)] for x in range (N)]
	if (len(string) != (N * N)):
		print "invalid table"
		sys.exit(2)
	for i in range(N):
		for j in range(N):
			puzzle[i][j] = int(string[counter])
			counter += 1

	return puzzle

def getNumberOfVariables(digit, row, column):
	return (N * N * row) + (N * column) + digit

def eachCell():
	for row in range (N):
		for column in range (N):
			clause = [];
			for value in range (1, N+1):
				clause.append(getNumberOfVariables(value, row, column))
			solution.append(clause)

def oncePerColumn():
	for col in range (N):
		for value in range (1, N+1):
			for row in range (N-1):
				for nrow in range(row+1):
					solution.append([-getNumberOfVariables(value,row,col), -getNumberOfVariables(value, nrow, col)])

def oncePerRow():
	for row in range (N):
		for value in range (1, N+1):
			for column in range (N-1):
				for ncol in range(column+1):
					solution.append([-getNumberOfVariables(value, row, column), -getNumberOfVariables(value, row, ncol)])

def oncePerGrid():
	for value in range (1, N+1):
		for xbox in range(C):
			for ybox in range(C):
				for i in range(C):
					for j in range(C):
						for k in range(i+1, C):
							for l in range(C):
								solution.append([-getNumberOfVariables(value, C * xbox + i, C * ybox + j), -getNumberOfVariables(value, C * xbox + k, C * ybox + l)])

def addFromGrid():
	global puzzle
	for row in range(N):
		for column in range(N):
			if(puzzle[row][column] > 0):
				solution.append([getNumberOfVariables(row, column, puzzle[row][column])])

def minimalEncoding():
	addFromGrid()
	eachCell()
	oncePerRow()
	oncePerColumn()
	oncePerGrid()

def main(argv):
	inputfile = ''
	outputfile = ''
	global N
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hi:o:n:")
	except getopt.GetoptError:
		print 'minimalSolver.py -i <inputfile> -o <outputfile> -n <number of rows>'
		sys.exit(2)
	for option, arg in opts:
		if option in ("-i"):
			inputfile = arg
		elif option in ("-o"):
			outputfile = arg
		elif option in ("-n"):
			N = int(arg)
		elif option in ("-h"):
			print 'minimalSolver.py -i <inputfile> -o <outputfile> -n <number of rows>'
			sys.exit(2)
	if ((N is 0) or (inputfile is '') or (outputfile is '')):
		print 'ffminimalSolver.py -i <inputfile> -o <outputfile> -n <number of rows>'
		sys.exit(2)

	#try:
	global puzzle
	string = read(inputfile)
	C = math.sqrt(N)
	puzzle = parse(string)
	print puzzle
	minimalEncoding()
	write() #write to intermediate file for miniSAT reading
	#call(["miniSAT", "mid.txt", outputfile]) #assuming this is how the minisat accepts things.

	#except:
	#	print "failed read. for help use -h option"

if __name__ == "__main__":
	main(sys.argv[1:])

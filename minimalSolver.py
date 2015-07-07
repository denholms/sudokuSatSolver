from subprocess import call
import sys, getopt, math

# call(["minisat", "arg", "arg"])
# minimalSolver.py -i inputfile -o outputfile -n number

# Every row contains the number once
# Every column contains the number once
# Every number appears once in every grid

N = 9

def read (file):
	f = open(file, "r")
	buff = f.readline()
	while (buff != ''):
		string += buff
		buff = f.readline()
	f.close()
	return string

def write (file, solution):
	f = open(file, "rw+")
	for i in range(N):
		for j in range(N):
			f.write(solution[i][j])
			f.write(" ")
		f.write("\n")
	f.close()


def parse(string):
	string.replace("\n", "").replace("*", "0").replace(".", "0").replace("*", "0").replace("?", "0")
	
	counter = 0
	puzzle = [[0 for x in range (N)] for x in range (N)]
	if (string.len != (N * N)):
		print "invalid table"
		sys.exit(2)
	for i in range(N):
		for j in range(N):
			puzzle[i][j] = int(string[counter])

	return puzzle


def main(argv):
	inputfile = ''
	outputfile = ''
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
	try:
		string = read(inputfile)
	except:
		print "failed read"
	
	parse(string)

	print 'Output file is "', outputfile

if __name__ == "__main__":
	main(sys.argv[1:])

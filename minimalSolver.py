from subprocess import call
import sys, getopt

# call(["minisat", "arg", "arg"])
# minimalSolver.py -i inputfile -o outputfile -n number

# Every row contains the number once
# Every column contains the number once
# Every number appears once in every grid

N = 3

def read (file):
	f = open(file, "r")
	buff = f.readline()
	while (buff != ''):
		string += buff
		buff = f.readline()
	return string



def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:n:")
   except getopt.GetoptError:
   	print 'minimalSolver.py -i <inputfile> -o <outputfile> -n <number of rows/cols>'
   	sys.exit(2)
   for option, arg in opts:
   	if option in ("-i"):
   		inputfile = arg
   	elif option in ("-o"):
   		outputfile = arg
    elif option in ("-n"):
      	N = int(arg)
	try:
		string = read(inputfile)
	except:
		print "failed read"


   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
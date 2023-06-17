from src.FunctionHandler import FunctionHandler
from src.LinearSolver import LinearSolver


def main():
	
	# fn = "2x^3-2x-5"
	fn = input("Enter an Equation (with X): ")
	fh = FunctionHandler(fn)

	rpn = fh.getFunctionRPN()
	ls = LinearSolver(rpn)
	
	deci = 8
	a = 1
	b = 2
	atol = 10**(-deci)
	p,k = ls.bisec([a,b], atol = atol)
	print("Results\t\t\tIterations")
	print(str(p)+"\t"+str(k))
	


if __name__ == "__main__":
	main()
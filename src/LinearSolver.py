
from src.Solver import Solver
import math


class LinearSolver(Solver):

		def __init__(self, rpn: list[str]) -> None:
			super().__init__()
			self.function = rpn
	
		def eval(self, var: int = 1) -> float:
			""" 
			evaluates a list of token representing a math expresion in Reverse Polish Notation
			currently does not support floats/number with decimal points.  Allows variable inputs
			param var:  if the function contains a letter variable, replace it with var, defaults to 1
			return:     a float of the value evaluated from self.function
			"""
			eval_stack = []

			for token in self.function:
				if token.isdigit():
					eval_stack.append(float(token))
				elif token.isalpha():
					eval_stack.append(var)
				else:
					b = eval_stack.pop()
					a = eval_stack.pop()

					match token:
						case "^":
							eval_stack.append(pow(a,b))
						case "*":
							eval_stack.append(a*b)
						case "/":
							eval_stack.append(a/b)
						case "+":
							eval_stack.append(a+b)
						case "-":
							eval_stack.append(a-b)
			
			return eval_stack[0]


		def bisec(self, range: list, atol:float = -1.0, ftol:float = -1.0) -> float:
			if atol <= 0 and ftol <= 0:
				print("Error: please specify a tolerance that is less than 1 for atol, rtol, or ftol")
				return None
			a,b = range

			if a >= b:
				print("Error: the first value in range must be less than the second value")
				return None

			equation = (lambda x: self.eval(x))
			fa = equation(a)
			fb = equation(b)



			if fa * fb >= 0:
				print("Error: the range specified does not change sign with the euqation given")
				return (None,None)
			k = 0
			max_iter =  math.ceil((math.log10(b-a)-math.log10(atol))/(math.log10(2)))
			# max_iter =  100
			while(k < max_iter):
				k += 1
				p = (b+a)/2
				fp = equation(p)
				if abs(fp) < ftol:
					return (p,k)
				val = fa * fp
				if val < 0:
					b = p
				elif val > 0:
					a = p
				else:
					return (p,k)
				if abs(b-a) < atol:
					return (p,k)

			print("Error: Max Iteration Exceeded: k =%d, p = %f"%(k,p))
			return (None,None)
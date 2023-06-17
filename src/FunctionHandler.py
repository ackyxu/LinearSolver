class FunctionHandler:
    
	xLocations:  list[int]=  []
 
	def __init__(self,fn) -> None:
     
		self.functionRPN: list[str] = self.parser(fn)
		self.findX()

		
	def parser(self, input: str) -> list:
		""" 
		parses an input math expression into a list of nodes to be used for math operations
		uses shunting yards algo.
		currently does not support floats/number with decimal points
		idea from https://www.engr.mun.ca/~theo/Misc/exp_parsing.htm
		and https://en.wikipedia.org/wiki/Shunting_yard_algorithm
		param str:  an input str of valid math expression (integers)
		return:     a list of operations, in Reverse Polish Notation
		"""

		# stack for output
		operand = []
		# operator stack, 0 indicates the end
		operator = [0]
		# size of the input string
		input_size = len(input)
		precedence_dict = {
			"^" : 4,
			"*" : 3,
			"/" : 3,
			"+" : 2,
			"-" : 2,

		}
		if input[0]!= " ":
			operand.append(input[0])
		for i in range(1,input_size):

			token = input[i]
			if token == ' ':
				continue
			elif token.isdigit():
				if input[i-1].isdigit():
					operand[-1] += token
				else:
					operand.append(token)

			elif token.isalpha():
				operand.append(token)

				if (operand[i-1] != 0 and operand[i-1].isdigit()):
					operator.append("*")  

				for j in range(len(operator)-1,-1, -1):
					if operator[j] == "(" or operator[j] == 0:
						break
					# else:
					# 	break
	
				

			elif token in precedence_dict:
				for j in range(len(operator)-1,0, -1):
					if operator[j] == "(" or operator[j] == 0:
						break
					elif precedence_dict[operator[j]] >= precedence_dict[token] and token != "^":
						operand.append(operator.pop())
					else:
						break
				operator.append(token)

			elif token == ")" :
				for j in range(len(operator)-1,0, -1):
					if operator[j] == "(":
						operator.pop()
						break
					else:
						operand.append(operator.pop())
				# if the loop does not find a left bracket, hence we have a mismatch brackets
				else:
					print("Error: Mismatch brackets, aborting")
					return None

			elif token == "(":
				operator.append(token)
			# print(f"\ntoken: {token}")
			# print(f"operand:{operand}")
			# print(f"operator:{operator}")
			# print(" ")
			

		for i in range(len(operator)-1):
			operand.append(operator.pop())
	
		return operand
	
	def findX(self):
		"""
  		Find the location of x in self.functionRPN and appends them to self.xLocations
		Only support lower case x, and only x
	
		"""
		for i in range(len(self.functionRPN)):
			if self.functionRPN[i] == 'x':
				self.xLocations.append(i)
	
	def getXLocations(self):
		return self.xLocations

	def getFunctionRPN(self):
		return self.functionRPN
	


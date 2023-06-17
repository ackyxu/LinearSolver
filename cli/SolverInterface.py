class SolverInterface:
	cont: bool = True
	features: list[tuple(str,str)] = [ 
		"Linear Solver": "linsolv",
	]
	def __init__(self) -> None:
		self.runProgram()

	
	def runProgram(self):
		
		while(self.cont):
			self.displayOptions()
			input = self.getUserInput()
			
	

	def displayOptions(self):
		print("Welcome To Solver CLI!")
		self.printOptions()

	


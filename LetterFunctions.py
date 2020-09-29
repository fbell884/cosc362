import sys
import os
import math
from string import whitespace

"""
	This is the document string for this file. 
	This will serve as the library of functions that are needed by the letter writing main script. 
"""

# ========================================================================
# Define a Class
# ========================================================================

class Address:
	def __init__(self, First, Last, ADLine1, ADLine2):
		self.First = First
		self.Last = Last
		self.ADLine1 = ADLine1
		self.ADLine2 = ADLine2

	def dumpAddress(self):
		print ("Address Info: ")
		print (self.First, " ", self.Last)
		print (self.ADLine1, "\n", self.ADLine2)


class DocumentText:
	def __init__(self,address):
		self.address = address

		self.header = ("\\documentclass[12pt]{article} \n" 
			+ "\\usepackage{geometry} \n" 
			+ "\\geometry{hmargin={1in,1in}, vmargin={2in,1in}}\n" 
			+ "\\begin{document}\n\n")
		
		self.MyAddress = "10 South 10th Street\n\n \\vskip.5in \n\n"

		self.toAddress = (self.address.First + " " + self.address.Last + "\n\n"
				+ self.address.ADLine1 + "\n\n" 
				+ self.address.ADLine2 + "\n\n")

		self.date = "\\vskip.5in \n \\today \n\n \\vskip.5in \n\n"

		self.footer = "\\end{document} \n"

	def WriteLetter(self):
		LetterOutName = str(self.address.Last.lstrip(' '))+".tex"
		LetterFile = open(LetterOutName, "w")
		LetterFile.write(self.header)
		
		# More to come
				
		LetterFile.write(self.MyAddress)
		LetterFile.write(self.toAddress)
		LetterFile.write(self.date)
	
		LetterFile.write(self.footer)
		LetterFile.close()

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



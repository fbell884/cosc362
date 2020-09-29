
from LetterFunctions import *

"""
	This is a script to do a small mail merge to make custom letters to magic beings.
	To run: 
	[user@machine directory]$ python MainLetterScript.py <CSV File Address List>
"""
# =================================================================================================
# READ IN COMMAND LINE ARGUMENTS
# =================================================================================================

if len(sys.argv) != 2: 
	print("To Run: python MainLetterScript.py AddressList.txt")
else:
	print("Using addresses from the file", str(sys.argv[1]))
	dataFile = str(sys.argv[1])	

# =================================================================================================
# OPEN FILES
# =================================================================================================

AddressData = open(dataFile, "r")

# =================================================================================================
# READ DATA LINE BY LINE
# =================================================================================================

print("Reading from file: " + dataFile)

AddressList = []
for line in AddressData.readlines():
	First, Last, Address1, Address2 = map(str, line.split(','))
	CurrentAddress = Address(First, Last, Address1, Address2)
	# CurrentAddress.dumpAddress()
	AddressList.append(CurrentAddress)

for item in AddressList: 
	item.dumpAddress()	   
# =================================================================================================
# WRITE OUT THE FORM LETTERS
# =================================================================================================

for item in range(len(AddressList)):
	Letter = DocumentText(AddressList[item])
	Letter.WriteLetter()



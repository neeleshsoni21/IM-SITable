###################################
# Script to extract representation 
# from the rmf3 file
#
# neelesh soni - Salilab - UCSF
# neelesh@salilab.org
###################################

import sys
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import OrderedDict

from LoadArguments import LoadArguments
from Representation import GetRepresentation

def main():

	LA = LoadArguments()
	#print(LA.__doc__)

	args = LA.get_arguments()

	Rep = GetRepresentation(args)
	return


if __name__ == '__main__':
	main()
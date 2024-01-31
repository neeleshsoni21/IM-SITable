"""[summary]

[description]
"""
import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

class LoadArguments:
	"""This class loads the command line and other arguments.

	"""

	def __init__(self):
		"""[summary]
		
		[description]
		"""
		self.parse_commandline_arguments()

		self.validate_arguments()

		return

	def validate_arguments(self):
		"""[summary]
		
		[description]
		"""

		#TODO: Do the validatory checks here for the input arguments
		print("RMF File:",self.args.rmffile)
		print("Output Dir:",self.args.outdir)
		
		return

	def parse_commandline_arguments(self):
		"""
		Command Line arguments Definitions
		
		"""

		# Parse commandline Inputs
		parser_obj = ArgumentParser(description=__doc__, formatter_class=RawDescriptionHelpFormatter)

		parser_obj.add_argument("-i", "--rmffile", default=None, help="RMF file containing good scoring models")

		parser_obj.add_argument("-o", "--outdir", default=None, help="Output directory")

		self.args = parser_obj.parse_args()

		self.args.rmffile = os.path.abspath(self.args.rmffile)
		self.args.outdir = os.path.abspath(self.args.outdir)
		
		return 

	def get_arguments(self):
		"""[summary]
		
		[description]
		
		Returns:
			[type]: [description]
		"""

		return self.args


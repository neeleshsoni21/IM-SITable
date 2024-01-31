
import IMP
import RMF
import IMP.rmf
import IMP.core
import IMP.atom


class GetRepresentation:
	"""This class loads the command line and other arguments.

	"""

	def __init__(self, args):
		"""[summary]
		
		[description]
		"""

		self.args = args

		self.load_single_rmf_file()

		return

	def load_single_rmf_file(self):
		"""[summary]
		
		[description]
		"""

		model = IMP.Model()
		
		rh = RMF.open_rmf_file_read_only(self.args.rmffile)

		self.no_of_frames = rh.get_number_of_frames()

		self.hier = IMP.rmf.create_hierarchies(rh, model)[0]
		IMP.atom.show_with_representations(self.hier)
		IMP.atom.get_by_type(self.hier)

		NOTE either parse the log file or traverse the tree to get that file

		Then create a graph or save representation while traversing
		#print(IMP.atom.show_as_graphviz(self.hier,out=self.args.outdir+'file'))

		#self.hier = IMP.rmf.create_hierarchies(rh, model)
		#print(IMP.atom.get_representations(self.hier))

		#Only load first frame as representation would be same acros frames
		#frid = 0
		#IMP.rmf.load_frame(rh, RMF.FrameID(frid))

		#self.get_particles_all_representations()

		#model.update()
		#del model

		return


	def get_particles_all_representations(self):
		"""
		
		"""
		#for mol in IMP.atom.get_by_type(self.hier, IMP.atom.CHAIN_TYPE):
		#	print(mol)
		
		for mol in IMP.atom.get_by_type(self.hier, IMP.atom.MOLECULE_TYPE):

			print("Mol:",mol)
			copy = IMP.atom.Copy(mol).get_copy_index()
			molname = mol.get_name().upper()+'.'+str(copy)
			chainid = IMP.atom.get_chain(mol).get_id()

			'''
			sel = IMP.atom.Selection(mol, resolution=1)
			for p in sel.get_selected_particles():
												
				IMP.core.XYZ(p).get_coordinates()
				resSeq = int(IMP.atom.Residue(p).get_index())
				resnum = int(p.get_name())
			'''
						
		return


	def get_number_of_frames(self):

		return self.no_of_frames

import argparse
from Bio import PDB
import os

argParser = argparse.ArgumentParser(description="This script takes an input pdb file containing structure of a nucleic acid in full atom representation and saves to an output file path its coarse grain representation")
argParser.add_argument("-i", "--input", dest = "inputFilePath" , required=True, help="input pdb file to be transformed into coarse grain representation", type=str)
argParser.add_argument("-o", "--output", dest = "outputFilePath" , required=True, help="path for output pdb file with in coarse grain format", type=str)


args = argParser.parse_args()

pdb_parser = PDB.PDBParser()

structureId = os.path.splitext(os.path.basename(args.inputFilePath))[0]
fullAtomStructure = pdb_parser.get_structure(structureId,args.inputFilePath)

print(fullAtomStructure.id)

coarseGrainStructure = PDB.Structure.Structure("430d_cg")

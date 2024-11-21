import argparse
from Bio.PDB.PDBList import PDBList
from Bio import PDB

argParser = argparse.ArgumentParser(description="This script takes an input pdb file in full atom representation and saves to an output file path its coarse grain representation")
argParser.add_argument("-i", "--input", dest = "inputFilePath" , required=True, help="input pdb file to be transformed into coarse grain representation", type=str)
argParser.add_argument("-o", "--output", dest = "outputFilePath" , required=True, help="path for output pdb file with in coarse grain format", type=str)


args = argParser.parse_args()

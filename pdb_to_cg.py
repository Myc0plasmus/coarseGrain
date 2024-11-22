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


coarseGrainStructure = PDB.Structure.Structure(structureId + "_cg")

for model in fullAtomStructure:
    newModel = PDB.Model.Model(model.id)
    coarseGrainStructure.add(newModel)
    for chain in model:
        newChain = PDB.Chain.Chain(chain.id)
        newModel.add(newChain)
        for i,res in enumerate(chain):
            if not res.get_resname() in ["A","C","G","U"]:
                continue
            newResidue = PDB.Residue.Residue((" ", i+1, " "),res.get_resname(), " ")
            newChain.add(newResidue)
            # print(res.get_resname())
            # for atom in res.get_atoms():
            #     print(atom.get_name())
            if "P" in res:
                newResidue.add(res["P"])
            newResidue.add(res["C4'"])
            if res.get_resname() in ["U","C"]:
                newResidue.add(res["N1"])
                newResidue.add(res["C2"])
                newResidue.add(res["C4"])
            else:
                newResidue.add(res["N9"])
                newResidue.add(res["C2"])
                newResidue.add(res["C6"])

io = PDB.PDBIO()
io.set_structure(coarseGrainStructure)
io.save(args.outputFilePath)

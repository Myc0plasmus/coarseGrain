import argparse
from Bio import PDB
import os

argParser = argparse.ArgumentParser(description="This script takes an input pdb file containing structure of a nucleic acid in coarse grain representation and saves to an output file path its reconstructed full atom representation")
argParser.add_argument("-i", "--input", dest = "inputFilePath" , required=True, help="input pdb file to be transformed back into full atom representation", type=str)
argParser.add_argument("-o", "--output", dest = "outputFilePath" , required=True, help="path for output pdb file with in full atom representation", type=str)



args = argParser.parse_args()

pdb_parser = PDB.PDBParser()

template_residues = {
    "A": pdb_parser.get_structure("A", "templates/A_template.pdb")[0]["A"][26],
    "U": pdb_parser.get_structure("U", "templates/U_template.pdb")[0]["A"][11],
    "G": pdb_parser.get_structure("G", "templates/G_template.pdb")[0]["A"][24],
    "C": pdb_parser.get_structure("C", "templates/C_template.pdb")[0]["A"][29],
}

structureId = os.path.splitext(os.path.basename(args.inputFilePath))[0]
coarseGrainStructure = pdb_parser.get_structure(structureId,args.inputFilePath)

fullAtomStructure = PDB.Structure.Structure(structureId + "_cg")

sup = PDB.Superimposer()

for model in coarseGrainStructure:
    newModel = PDB.Model.Model(model.id)
    fullAtomStructure.add(newModel)
    for chain in model:
        newChain = PDB.Chain.Chain(chain.id)
        newModel.add(newChain)
        for i,res in enumerate(chain):
            if not res.get_resname() in ["A","C","G","U"]:
                continue
            fullAtomResidue = template_residues[res.get_resname()].copy()
            fullAtomResidue.id = (" ", i+1, " ")
            movingAtomList = [fullAtomResidue[atom.get_name()] for atom in res]
            fixedAtomList = [atom for atom in res]

            sup.set_atoms(fixedAtomList, movingAtomList)
            
            for atom in fullAtomResidue:
                atom.transform(sup.rotran[0], sup.rotran[1])
            newChain.add(fullAtomResidue.copy())


io = PDB.PDBIO()
io.set_structure(fullAtomStructure)
io.save(args.outputFilePath)

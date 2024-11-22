# Coarse grain transformer scripts - report 3 - task 3 - structural bioinfromatics

Scripts pdb_to_cg.py and cg_to_pdb.py can convert .pdb file to coarse grain representation and back respectively.

## Prerequisites 
activate the environment:
```
conda env create --file env.yml
conda active structural-bio-env
```
... and you're all set to go.

## Usage

Both scripts have built in manuals activated via:
```
python cg_to_pdb.py/pdb_to_cg.py --help
```

general usage for both scripts is as follows:

```
python <name of the script> --input <path to input pdb file> --output <path to output pdb file>
```

this expression will trigger the transformation and its direction (full atom to coarse grain or in reverse) is dictated by the script used.

## Example data

* `430d.pdb` - is the input file used for transformation to coarse grain representation
* `430d_cg.pdb` - is `430d.pdb` transformed to coarse grain
* `430d_rec.pdb` - is version of `430d_cg.pdb` reconstructed to full atom representation

Here is alignment score (rmsd) or original structure and reconstructed one:

![image](https://github.com/user-attachments/assets/c73a186b-be00-4c5f-966a-2026225c90de)
 

# renumbered_PDB
Many times the numbering of the amino acids in a protein structure differs from your numbering. For example for a certain protein you refer to Lys 67 while in the PDB file the same Lys is numbered as Lys 68. This program allows you to change the numbering of the amino acids in a PDB file. 

Instruction for Biologist:
This is a stand alone program. Feel free to modified it to meet your needs. 
1) Install python.
2) Make a folder and move the PDB files you want to renumbered into this folder.
3) Copy the file renumbered_PDB.py in the above folder.
4) Start a terminal. Use cd <folder_name> until you are in the folder containing the .py file. Write >perl renumbered_PDB.py.
5) The program reads the PDB files one by one. It will asked you to renumber the aa chain by chain.
6) It will be create a new folder inside the original folder named modified_PDB.
7) Inside this folder you will find your modified PDB file.

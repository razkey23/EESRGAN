import os
import sys 

import os
import shutil
#from shutil import copyfile,copy2,copy
def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

files = get_filepaths('/home/razkey23/cowc-gan/DetectionPatches_256x256/Potsdam_ISPRS')
for f in files:
    if ".txt" in f:
        print(f.split("/")[-1])
        if f.split("/")[-1]=="Potsdam_2_10_RGB.3.11.txt":continue
        shutil.copy( f , '/home/razkey23/cowc-gan/DetectionPatches_256x256/Potsdam_ISPRS/LR/x4/'+f.split("/")[-1])
        shutil.copy( f , '/home/razkey23/cowc-gan/DetectionPatches_256x256/Potsdam_ISPRS/HR/x4/'+f.split("/")[-1])
        shutil.copy( f , '/home/razkey23/cowc-gan/DetectionPatches_256x256/Potsdam_ISPRS/Bic/x4/'+f.split("/")[-1])
#print(files)


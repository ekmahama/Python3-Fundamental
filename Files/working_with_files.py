import os
import shutil

folder_original = "./Functions"
folder_destination ="./CleanUp"
if(not os.path.exists(folder_destination)):
    os.mkdir(folder_destination)

for entry in os.scandir(folder_original):
    loc_orig = os.path.join(folder_original, entry.name)
    loc_dest = os.path.join(folder_destination, entry.name)
    if os.path.isfile(loc_orig):
        shutil.copy(loc_orig, loc_dest)
    
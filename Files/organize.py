import os
import shutil

# Path of the desktop
desktop_path = os.path.expanduser("~/Desktop")

# Build dictionary of file extension and corresponding folder
folders = {
    "Images":[".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".doc", ".pdf","docx",".txt"],
    "Archives":[".zip", ".rar"]
}


# Create subfolder if they don't exist
for folder in folders:
    folder_path = os.path.join(desktop_path, folder)
    if not os.path.exists(folder_path):
        print(folder_path)
        #os.makedirs(folder_path)

# Move files
for file_name in os.scandir(desktop_path):
    orig_file_path = os.path.join(desktop_path, file_name)
    if os.path.isfile(orig_file_path):
        for folder_name, extenstions in folders.items():
            for extenstion in extenstions:
                if file_name.endswith(extenstion):
                    dest_folder = os.path.join(desktop_path, folder_name)
                    print(dest_folder)
                    #shutil.copy(orig_file_path,dest_folder)
# This code steps through the Downloads folder and seperates them into appropriate folders

import os
import shutil

# Change directory
os.chdir("/Users/Oz/Downloads")

#check files in  directory
files = os.listdir()

#list of extension (You can add more if you want)
file_extentions = {
    "images": [".gif", ".jpg", ".jpeg",".png" ],
    "videos": [".avi",".mp4", ".mkv"],
    "musics": [".mp3", ".wav"],
    "zip": [".rar", ".tar", ".tgz", ".zip" ],
    "documents": [".csv", ".doc", ".docx", ".odt", ".ppt", ".pptx", ".pdf", ".txt",  ".xlsx", ".xls"],
    "programs": [".py", ".app"]
}


#sort to specific folder depend on extenstions

def sort_file(file):
    keys = list(file_extentions.keys())
    for key in keys:
        for ext in file_extentions[key]:
            # print(ext)
            if file.endswith(ext):
                return key


#iterate through each file in downloads
for file in files:
    dist = sort_file(file)
    if dist:
        try:
            shutil.move(file, "../" + dist)
        except:
            print(file + " is already exist")
    else:
        try:
            shutil.move(file, "../download-sorting/others")
        except:
            print(file + " is already exist")

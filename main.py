import os
import shutil
import re
from datetime import datetime,date
from file_extensions import getExtDict
from pathlib import Path
import time
from sys import platform

class Cleaner:
    def __init__(self, path, dir_folders, dict_ext, recent_date):
        self.path = path
        self.files = []
        self.dir_folders = dir_folders
        self.dict_ext = dict_ext
        self.recent_date = recent_date
        self.currentTime = datetime.now()
        start_time = time.time()

        user_input = self.userInput()
        flag = True
        while(flag):
            if user_input == "c":
                self.dirMaker()
                self.CreateFolder()
                self.updateRecent()
                self.folderOrginizer()
                duration = self.currentTime - datetime.now()
                print("This Program took about ", time.time() - start_time)
                flag = False
            elif user_input == "u":
                self.dirMaker()
                self.unpackFiles()
                duration = self.currentTime - datetime.now()
                print("This Program took about ", time.time() - start_time)
                flag = False
            else:
                print("Please select either c for clean or u for unpack")
                user_input = self.userInput()

    def dirMaker(self):
        try: 
            os.chdir(self.path)
            self.files = os.listdir()
        except:
            print("Make sure the folder destination is correct")

    def userInput(self):
        val = input("Would you like to clean or unpack the files from the Folder?(c/u): ")
        return val.lower()

    def unpackFiles(self):
        # check for the operation system to concate the right path syntax
        if platform == "win32":
            file_syntax = "\\"
        else: 
            file_syntax = "/"

        if os.path.isdir(self.path + file_syntax + "OTHERS"):
            for file in self.files:
                full_path = self.path + file_syntax + file
                subfile = os.listdir(full_path)
                for index in range(len(subfile)):
                    path_to_each_files = full_path + file_syntax + subfile[index]
                    shutil.move(path_to_each_files,self.path)
                os.rmdir(full_path)
        else:
            print("There are no right files to unpack at this time")

    def CreateFolder(self):
        for dir in self.dir_folders:
            if not os.path.isdir("./{}".format(dir)):
                os.mkdir("./{}".format(dir))
        print("Directories have been created successfuly.")
    
    def getTimeDiff(self,f):
        self.currentTime
        mtime = os.path.getmtime(f)
        file_time = datetime.fromtimestamp(mtime)
        diff = self.currentTime - file_time
        return diff.days

    def updateRecent(self):
        if not os.path.isdir("./RECENT"):
            return False
        else:
            os.chdir(self.path+"/RECENT")
            for f in os.listdir():
                file_birth = self.getTimeDiff(f)
                if file_birth > self.recent_date:
                    shutil.move(f,self.path)
        os.chdir(self.path)

    def folderOrginizer(self):
        dict_ext = self.dict_ext
        for f in self.files:
            # remove duplicates
            if re.search("\(\d+\)", f):
                if os.path.isdir(f):
                    shutil.rmtree(f)
                else:
                    os.remove(f) 
            else:
                file_birth = self.getTimeDiff(f)
                moved_file_flag = False
                name, extension = os.path.splitext(f)
                for key,val in dict_ext.items():
                    if str.lower(extension) in val:
                        shutil.move(f, "./{}/{}".format(key,f)) 
                        moved_file_flag = True
                if name not in self.dir_folders and moved_file_flag == False:
                    if os.path.isdir(name):
                        shutil.move(f, "./FOLDERS/{}".format(f))
                    elif file_birth < self.recent_date:
                        shutil.move(f, "./RECENT/{}".format(f))
                    else:
                        shutil.move(f,"./OTHERS/{}".format(f))

# TODO: Build an unpacker, allow the user to unpack files from all or certain folders in case they want to add more folders later on.
source = "C:\\Users\\thien.le\\Downloads"
dict_ext = getExtDict()
DIRS = list(dict_ext.keys()) + ["FOLDERS", "OTHERS","RECENT"]
recent_date = 2
if __name__ == "__main__":
    folders_cleaner = Cleaner(source, DIRS,dict_ext, recent_date)

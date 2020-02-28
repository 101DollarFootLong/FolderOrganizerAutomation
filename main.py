import os
import shutil
import re
from datetime import datetime,date
from file_extensions import getExtDict

class Cleaner:
    def __init__(self, path, dir_folders, dict_ext, recent_date):
        self.path = path
        self.files = []
        self.dir_folders = dir_folders
        self.dict_ext = dict_ext
        self.recent_date = recent_date
        self.currentTime = datetime.now()

        self.dirMaker()
        self.CreateFolder()
        self.folderOrginizer()
        duration = self.currentTime - datetime.now()
        print("This Program took about ", duration.seconds)

    def dirMaker(self):
        os.chdir(self.path)
        self.files = os.listdir()
        
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

    # TODO: Set a flag if the user want their duplicate files to be remove
    def folderOrginizer(self):
        dict_ext = self.dict_ext
        for f in self.files:
            if re.search("\(\d+\)", f):
                print(f)
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
path = "/Users/thienle/Desktop/MainDesktop/DataScience/Python/FolderOrganizerAutomation/TestFolder"
dict_ext = getExtDict()
DIRS = list(dict_ext.keys()) + ["FOLDERS", "OTHERS","RECENT"]
recent_date = 2
if __name__ == "__main__":
    folders_cleaner = Cleaner(path, DIRS,dict_ext, recent_date)

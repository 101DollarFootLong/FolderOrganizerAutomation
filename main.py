import os
import shutil
import re
from datetime import datetime,date
from file_extensions import getExtDict

class Cleaner:
    def __init__(self, path, dir_folders, dict_ext):
        self.path = path
        self.files = []
        self.dir_folders = dir_folders
        self.dict_ext = dict_ext

        self.dirMaker()
        self.CreateFolder()
        self.folderOrginizer()

    def dirMaker(self):
        os.chdir(self.path)
        self.files = os.listdir()
        # Clean out duplicates
        [os.remove(x) for x in self.files if re.search("\(\d{1}\)", x)]
        
    def CreateFolder(self):
        for dir in self.dir_folders:
            if not os.path.isdir("./{}".format(dir)):
                os.mkdir("./{}".format(dir))
        print("Directories have been created successfuly.")
    
    def getTimeDiff(self):
        for f in self.files:
            currentTime = datetime.now()
            mtime = os.path.getmtime(f)
            file_time = datetime.fromtimestamp(mtime)
            diff = currentTime - file_time
            return diff.days

    def folderOrginizer(self):
        dict_ext = self.dict_ext
        for f in self.files:
            name, extension = os.path.splitext(f)
            for key,val in dict_ext.items():
                if extension in val:
                    shutil.move(f, "./{}/{}".format(key,f))   
                else:
                    if name not in self.dir_folders:
                        if os.path.isdir(name):
                            shutil.move(f, "./FOLDERS/{}".format(f))
                        elif self.getTimeDiff() < 5:
                            print("Test",self.getTimeDiff())
                            shutil.move(f, "./RECENT/{}".format(f))
                        else:
                            shutil.move(f,"./OTHERS/{}".format(f))

path = "/Users/thienle/Desktop/MainDesktop/DataScience/Python/FolderCleanUp/Test"
dict_ext = getExtDict()
DIRS = list(dict_ext.keys()) + ["FOLDERS", "OTHERS","RECENT"]
if __name__ == "__main__":
    folders_cleaner = Cleaner(path, DIRS,dict_ext)

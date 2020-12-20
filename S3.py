import sys
import os
import glob
from pathlib import Path
import transcode
from multipleVideo import multipleVideo 
from stream import stream
EXIT = 0
TRANSCODE = 1
MULTIPLE = 2
STREAM = 3

class iodir:
    inp : str
    path : str
    files : list
    outputFolder : list

    def __init__(self,inp,path,files):
        self.inp=inp
        self.path=path
        self.files=files # indexed files
        self.outputFolder = ''

    def refresh(self,path):
        files = [i for i in os.listdir(path) if i.endswith('.mp4') ]  # ignore random files
        dyr.files = [(s + 1, i) for (s, i) in enumerate(files)]

    def printfiles(self, path):
        self.refresh(path)
        for file in dyr.files:
            print('{} - {}'.format(file[0], file[1]))
    
    def chooseinput(self,var='file'):
        if 'file'==var:
            self.printfiles(dyr.path)
            aux = int(input("Which file you want as a input?\n"))
            self.inp = self.files[aux-1][1]
            name,_=check_ext_name(self.inp)
            self.outputFolder = self.path / "Results" / name
            self.outputFolder.mkdir(parents=True, exist_ok=True)
        elif 'folder'== var:
            self.printfiles(dyr.path/"Results")
            aux = int(input("Which folder contains the videos?\n"))
            self.outputFolder = self.path / "Results" / self.files[aux-1][1]
            print("This folder contains the following files:\n")
            self.printfiles(self.outputFolder)

#Define directories   
def setDir():
    name = "BBB_720p.mp4"
    path =  Path.cwd()#set path to Data folder
    #for each file in folder get input path (BBB.mp4)
    file_path= [ subp for subp in path.iterdir() if subp.match(name)]
    file_path.sort()
    files = [i for i in os.listdir(path) if i.endswith('.mp4') ]    # avoid random files
    files = [(s + 1, i) for (s, i) in enumerate(files)]#Make a enumerated list of the files in the folder
    return iodir(str(file_path[0]),path,files)

def check_ext_name(name):
    split = name.split('.')
    #Check if there is extension
    if(len(split) > 1):
        file_extension = split.pop()
    else:
        file_extension = None
    return split[0],file_extension


if __name__ == "__main__": 
    dyr=setDir()#set directories
    x = int(input("[1]Transcode\n[2]Multiple Video\n[3]Stream\n"))
    while not x == EXIT:
        if x == TRANSCODE:
            dyr.chooseinput(var='file')
            transcode.transcode(dyr.outputFolder,dyr.inp)
        elif x == MULTIPLE:
            dyr.chooseinput(var='folder')
            multipleVideo(dyr.outputFolder,dyr.files)
        elif x == STREAM:
            stream(dyr.path/"cut_BBB.mp4")
        x = int(input("[1]Transcode\n[2]Multiple Video\n[3]Stream\n"))





    
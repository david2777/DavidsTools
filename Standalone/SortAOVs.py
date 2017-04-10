"""Moves AOVs into their own folders.
Made for use with Redshift's CMD Render tool."""
import glob
import os
import shutil
from collections import defaultdict

def find_files(filePath, ext):
    if os.path.isfile(filePath):
        return None
    searchPath = os.path.join(filePath, ext)
    return glob.glob(searchPath)

def sort_files(fileList):
    fileDict = defaultdict(list)
    for f in fileList:
        fPath, fName = os.path.split(f)
        fSplit = f.split(".")
        if len(fSplit) > 3:
            fileDict[fSplit[1]].append(f)
    return fileDict if fileDict else None

def build_directories(fileDict, filePath):
    responseList = []
    for dirName in fileDict.keys():
        newDir = os.path.join(filePath, dirName)
        newDir = os.path.abspath(newDir)
        if not os.path.exists(newDir):
            os.mkdir(newDir)
        responseList.append(os.path.exists(newDir))
    return all(responseList)

def copy_files(fileDict):
    for k, valueList in fileDict.iteritems():
        for v in valueList:
            source = v
            head, tail = os.path.split(v)
            dest = os.path.join(head, k, tail)
            shutil.copy2(source, dest)

if __name__ == "__main__":
    frameDir = raw_input("Path To Frames: ")
    frameDir = os.path.abspath(frameDir.replace("\"", ""))
    fList = find_files(frameDir, "*.exr")
    if fList:
        fDict = sort_files(fList)
        if fDict and build_directories(fDict, frameDir):
            copy_files(fDict)
        else:
            print "ERROR!"
    else:
        print "ERROR!"

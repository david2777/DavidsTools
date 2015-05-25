#Stadard
from glob import glob
import os
import shutil
from operator import itemgetter

#3rd Party (PIL)
from PIL import Image
from PIL.ExifTags import TAGS

"""
By David DuVoising for Python 2.7
I wrote this while making HDRI Spheres using PTGui. PTGui looks for bracketed exposures
using a repeateing patterns such as 100, 200, 300, 100, 200, 300. However, I didn't
have a fancy camera that did automatic bracketing so I found it easier to do
100, 200, 300, 300, 200, 100 which the software didn't like. So this script sorts
groups of bracketed exposures by their exposure time from the EXIF data on the images.
"""

def getKey(item):
    #Used in the doSort funciton for Tuple Sorting
    return item[1]

def getImages(folder):
    """
    Globs a bunch of image formats, once it finds an image for one of them it stops
    so that it dones't waste time. Returns a list of the file paths.
    """
    extentions = ["\\*.jpg", "\\*.cr2", "\\*.crw", "\\*.dng", "\\*.mrw", "\\*.raw"]
    imageList = []
    while imageList == []:
        for ext in extentions:
            for image in glob(folder+ext):
                image  = os.path.abspath(image)
                imageList.append(image)

    return imageList

def getExposures(imageList):
    """
    Reads the EXIF data from each image to try to find the exposure time.
    Returns a Dictionary with the image path as the key and the exposure as the value.
    """
    imageDict = {}
    for image in imageList:
        tempDict = {}
        i = Image.open(image)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            tempDict[decoded] = value

        try:
            exp = int(tempDict['ExposureTime'][1])
        except KeyError:
            raise Exception("Could not find ExposureTime EXIF Metadata on %s" %image)

        imageDict.update({image:exp})

    return imageDict

def doSort(imageList, imageDict, numberPerGroup, imagePath, mode):
    """
    Does the actual sorting and renaming. I found out that dictionarys are orderless
    so I end up converting my image dictionary to a tuple here.
    """
    #Takes the first image, splits it by . and then gets the last part of the list
    imageExt = "." + imageList[0].split(".")[-1]
    if mode == "copy":
        try:
            os.mkdir(imagePath + "\\BracketOutput\\")
        except WindowsError:
            pass

    #Here's where I found out dictionaries are orderless and converted it to a tuple.
    imageTuple = sorted(imageDict.items(), key = itemgetter(0))
    #i is the counter for the group number
    #j is the counter for the number of images
    i = 0
    j = 0
    while j < len(imageList):
        #k is the counter for the image number within the group
        k = 1
        imagePrefix = "FRAME_%s" %str(i).zfill(5)
        print imagePrefix
        tempTuple = imageTuple[j : j + numberPerGroup]
        tempTuple = sorted(tempTuple, key = getKey)
        for item in tempTuple:
            print item
            if mode == "copy":
                newName = imagePath + "\\BracketOutput\\" + imagePrefix + "_" + str(k).zfill(2) + imageExt
                shutil.copy2(item[0], newName)
            elif mode == "rename":
                newName = imagePath + "\\" + imagePrefix + "_" + str(k).zfill(2) + imageExt
                os.rename(item[0], newName)
            else:
                raise Exception("Bad mode given. Valid modes are copy and rename")
            k += 1
        i += 1
        j += numberPerGroup

    print "\n\n--------COMPLETE--------\n\n"

if __name__ == "__main__":
    imagePath = raw_input("Folder containing images: ")
    imagePath = os.path.abspath(imagePath)
    mode  = raw_input("Mode (copy or rename):")
    mode = mode.lower()
    numberPerGroup = int(input("Number of items per group: "))

    if os.path.exists(imagePath) == False:
        raise Exception("Error! Path not valid!")

    imageList = getImages(imagePath)

    if imageList == []:
        raise Exception("Images could not be found in specified directory!")

    if len(imageList) % numberPerGroup != 0:
        raise Exception("Images not divisable by number per group!")

    imageDict = getExposures(imageList)

    doSort(imageList, imageDict, numberPerGroup, imagePath, mode)

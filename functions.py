import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageGrab as imgGet

def readFile():
    zoneFile = open("zones.txt", "r")
    zones = []
    subregions = [[],[]]
    zones += [(zoneFile.readline())[:-1]]
    writeNext = 0
    currentRegion = 0
    for region in zoneFile:
        print(f"current region: {region}")
        if (region == "\n"):
            writeNext = True
            subregions += [[]]
            currentRegion += 1
        else:
            if (writeNext == True):
                zones += [region[:-1]]
                writeNext = False
            else:
                print("aaaaaaaa", currentRegion)
                subregions[currentRegion] += [region[:-1]]
    print(zones)
    for i in range(len(subregions)):
        print(subregions[i])
    '''
    print("Select region:")
    for i in range(len(zones)):
        print()'''
    zoneFile.close()
    
    return zones, subregions

def getRegion(zones, subregions):
    fileName = ""
    for i in range(len(zones)):
        print(f"[{i}]: {zones[i]}")
    while True:
        try:
            selectedZone = int(input("Select Region: "))
        except TypeError:
            print("Invalid, please enter a number.")
        else:
            if (0<selectedZone<(len(zones))+1):
                fileName += str(selectedZone) + "-"
                break
            else:
                print("Invalid, please enter a valid number.")
    print("Subregions:")
    for j in range(len(subregions)):
        print(zones[selectedZone-1][j])
    while True:
        try:
            selectedSubRegion = int(input("Select subregion: "))
        except TypeError:
            print("Invalid, please enter a number.")
        else:
            if (0<selectedSubRegion<(len(zones[selectedZone-1]))+1):
                fileName += str(selectedSubRegion)
                break
            else:
                print("Invalid, please enter a valid number.")
    
    fileName += ".png"
    return fileName

def search(region):
    # Grabbing image from clipboard, saving as a temporary file
    testMap = imgGet.grabclipboard()
    testMap.save("temp.png", "PNG")

    # Taking temporary image and preparing for comparison
    testImage = cv.imread("temp.png", cv.IMREAD_GRAYSCALE)
    fullMap = cv.imread(region, cv.IMREAD_GRAYSCALE)
    position = 0
    return position


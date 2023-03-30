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
        if (region == "\n"):
            writeNext = True
            subregions += [[]]
            currentRegion += 1
        else:
            if (writeNext == True):
                zones += [region[:-1]]
                writeNext = False
            else:
                subregions[currentRegion] += [region[:-1]]
    print(zones)
    for i in range(len(subregions)):
        print(subregions[i])

    zoneFile.close()
    
    return zones, subregions

## getRegion grabs region and subregion from user; returns filename
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
    # Resetting selectedZone to work with list index
    selectedZone -= 1

    # Printing subregions of the selected zone
    for j in range(len(subregions[selectedZone])):
        print(f"[{j+1}]: {subregions[selectedZone][j]}")

    # Data sanitation for subregion selection
    while True:
        try:
            selectedSubRegion = int(input("Select subregion: "))
        except TypeError:
            print("Invalid, please enter a number.")
        else:
            if (0<selectedSubRegion<(len(subregions[selectedZone]))+1):
                fileName += str(selectedSubRegion)
                break
            else:
                print("Invalid, please enter a valid number.")
    
    fileName += ".png"
    print(f"file name: {fileName}")
    return fileName

def search(regionFile):
    # Grabbing image from clipboard, saving as a temporary file
    testMap = imgGet.grabclipboard()
    testMap.save("temp.png", "PNG")

    # Taking temporary image and preparing for comparison
    testImage = cv.imread("temp.png", cv.IMREAD_GRAYSCALE)
    fullMap = cv.imread(regionFile, cv.IMREAD_GRAYSCALE)

    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    keypointQuery, desQuery = sift.detectAndCompute(testImage,None)
    keypointKnown, desKnown = sift.detectAndCompute(fullMap,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=100)   # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(desQuery,desKnown,k=2)
    
    # Need to draw only good matches; creating mask
    matchesMask = [[0,0] for i in range(len(matches))]
    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]
    draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,0,0),
                    matchesMask = matchesMask,
                    flags = cv.DrawMatchesFlags_DEFAULT)
    img3 = cv.drawMatchesKnn(testImage,keypointQuery,fullMap,keypointKnown,matches,None,**draw_params)

    # Display test image vs full map w/ matches
    plt.imshow(img3,),plt.show()
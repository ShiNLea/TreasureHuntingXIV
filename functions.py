import cv2
from matplotlib import pyplot as plt
import numpy as np

def zoneSelect():
    zoneFile = open("zones.txt", "r")
    zones = []
    zones += [(zoneFile.readline())[:-1]]
    writeNext = 0
    for region in zoneFile:
        if (region == "\n"):
            writeNext = True
        else:
            if (writeNext == True):
                zones += [region[:-1]]
                writeNext = False
            continue
    print(zones)
    '''
    print("Select region:")
    for i in range(len(zones)):
        print()'''
    zoneFile.close()
    

def search(area, map_image):
    position = 0
    return position


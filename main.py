import functions as func
import os
def main():
    
    zones, subregions = func.readFile()
    regionFile = func.getRegion(zones, subregions)
    quitCondition = func.search(regionFile)
    if (quitCondition == 1):
        print("Operation successful")
    else:
        pass
    
    print(os.getcwd())
main()

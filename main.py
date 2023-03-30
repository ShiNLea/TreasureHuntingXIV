import functions as func
def main():
    
    zones, subregions = func.readFile()
    regionFile = func.getRegion(zones, subregions)
    quitCondition = func.search(regionFile)
    if (quitCondition == 1):
        print("Operation successful")
    else:
        pass
    
main()

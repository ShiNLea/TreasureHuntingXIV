import functions as func

def main():
    zones, subregions = func.readFile()
    regionFileName = func.getRegion(zones, subregions)

main()

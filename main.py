import functions as func

def main():
    zones, subregions = func.readFile()
    regionFile = func.getRegion(zones, subregions)

main()

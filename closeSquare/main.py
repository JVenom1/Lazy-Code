from rectangleData import rectangleData


def findClosestSqr(area):
    area = float(area) # int case for rounding after decimal
    areaData =  rectangleData(area)
    minimum = areaData.dem2
    halfArea = int(int(area)/2)+1 # makes loop run for half the time
    
    for possDem in range(2, halfArea):
        areaData.dem1 = int(area)/possDem

        if possDem == minimum: # end clause
            areaData.dem2 = float(possDem)
            areaData.dem1 = areaData.dem1
            areaData.toString()
            return 1 # not prime

        if areaData.dem1 == int(areaData.dem1) and minimum > areaData.dem1: # checks if whole number and if minimum change is needed 
            minimum = areaData.dem1

    areaData.toString()
    return -1 # prime

def main():
    isWord = True
    while(isWord):
        userArea = input("Type an area:")
        try: # if error then not number
            userArea = float(userArea)
            isWord = False
            findClosestSqr(userArea)
        except:
            print("Not a number")


if '__main__':
    main()
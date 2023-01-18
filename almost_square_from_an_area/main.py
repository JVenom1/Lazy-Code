from rectangleData import rectangleData
import math

# takes an area and gives the 2 demensions that will represent the closest to a square shape


def findClosestSqr(area):
    area = float(area)  # int case for rounding after decimal
    areaData = rectangleData(area)
    minimum = areaData.dem2
    halfArea = int(int(area)/2)+1  # makes loop run for half the time

    # if perfect square (speeds up program)
    perfectDem = math.sqrt(area)
    if perfectDem == int(perfectDem):
        areaData.dem2 = perfectDem
        areaData.dem1 = perfectDem
        areaData.toString()
        return 1
    else:
        for possDem in range(2, int(halfArea)):
            areaData.dem1 = int(area)/possDem

            if possDem == minimum:  # end clause
                areaData.dem2 = float(possDem)
                areaData.dem1 = areaData.dem1
                areaData.toString()
                return 1  # not prime

            # checks if whole number and if minimum change is needed
            if areaData.dem1 == int(areaData.dem1) and minimum > areaData.dem1:
                minimum = areaData.dem1

    areaData.toString()
    return -1  # prime


def main():
    isWord = True
    while (isWord):
        userArea = input("Type an area: ")
        try:  # if error then not number
            userArea = float(userArea)
            isWord = False
        except:
            print("Not a number")
    if not isWord:
        findClosestSqr(userArea)
    input("Press \"Enter\" to exit")


main()

from rectangleData import rectangleData
import math

# takes an area and gives the 2 demensions that will represent the closest to a square shape


def findClosestSqr():
    areaData = rectangleData()
    minimum = areaData.dem2
    halfArea = int(int(areaData.area)/2)+1  # makes loop run for half the time

    # if perfect square (speeds up program)
    perfectDem = math.sqrt(areaData.area)
    if perfectDem == int(perfectDem):
        areaData.dem2 = perfectDem
        areaData.dem1 = perfectDem
        areaData.toString()
        return 1
    else:
        for possDem in range(2, int(halfArea)):
            areaData.dem1 = int(areaData.area)/possDem

            if possDem == minimum:  # end clause
                areaData.dem2 = float(possDem)
                areaData.dem1 = areaData.dem1
                areaData.toString()
                return 1  # not prime

            # checks if whole number and if minimum change is needed
            if areaData.dem1 == int(areaData.dem1) and minimum > areaData.dem1:
                minimum = areaData.dem1

    areaData.dem1 = areaData.area
    areaData.dem2 = 1
    areaData.toString()
    return -1  # prime


def main():
    findClosestSqr()
    input("Press \"Enter\" to exit")


main()

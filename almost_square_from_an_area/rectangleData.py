class rectangleData:
    def __init__(self) -> None:
        self.area = self.getArea()
        self.dem1 = 1         # demension 1 aka width
        self.dem2 = int(self.area)  # demension 2 aka length
        self.decimal = self.actualDecimal(self.area)
        self.area = self.area

    def getArea(self):
        isWord = True
        while (isWord):
            userArea = input("Type an area: ")
            try:  # if error then not number
                userArea = float(userArea)
                isWord = False
            except:
                print("Not a number")
            return userArea

    def actualDecimal(self, area):
        decimal = area - int(area)
        # will split [whole , decimal]
        roundAmount = len(str(area).split('.')[1])
        return round(decimal, roundAmount)

    def toString(self):
        print("\nArea:" + str(self.area) +
              " | Length:" + str(self.dem1) +
              " | Width:" + str(self.dem2) +
              " | Remaining:" + str(self.decimal))

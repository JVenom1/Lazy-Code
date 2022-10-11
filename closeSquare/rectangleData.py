class rectangleData:
    def __init__(self, area) -> None:
        self.dem1 = 1         # demension 1 aka width
        self.dem2 = int(area) # demension 2 aka length
        self.decimal = self.actualDecimal(area)
        self.area = area
    
    def actualDecimal(self, area): 
        decimal = area - int(area)
        roundAmount = len(str(area).split('.')[1]) # will split [whole , decimal]
        return round(decimal, roundAmount)

    def toString(self):
        print("\nArea:" + str(self.area) + 
        ", Length:" + str(self.dem1) + 
        ", Width:" + str(self.dem2) + 
        ", Remaining:" + str(self.decimal))
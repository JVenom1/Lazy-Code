class userInput:
    def __init__(self):
        pass
    
    def setSentance():
        sentance = input("Type a sentance: ")
        return sentance
    
    def setAsciiList():
        arrOfAscii = []
        num = " "
        while(num != ""): # when not "Enter"
            num = input("Type an ascii number [32 to 126]"+
                        "or press \"Enter\" when done: ")
            
            if(num == ""):
                break
            try:
                num = int(num)
            except:
                print("invalid number")
            arrOfAscii.append(num)
        if len(arrOfAscii) == 0: # demo data
            print("Since no data was typed: [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100] will be the demo data")
            arrOfAscii = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
        return arrOfAscii
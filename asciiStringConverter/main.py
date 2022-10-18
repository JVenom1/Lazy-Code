# "" -> []
from userInput import userInput


def stringToAscii(string, i=0, arrOfAsciiValues=[]):

    if i == len(string):
        print(arrOfAsciiValues)
    else:
        arrOfAsciiValues.append(ord(string[i]))
        stringToAscii(string, i+1, arrOfAsciiValues)

# [] -> ""
def asciiToString(asciiList, string="", i=0): 
    if i == len(asciiList):
        print(string)
    else:
        string += chr(asciiList[i])
        asciiToString(asciiList, string, i+1)

# changing text to ascii
def main():
    uI = userInput
    sentence = uI.setSentance() # makes user type a sentance
    stringToAscii(sentence)
    
    print() #new line
    
    #changing ascii list to text
    arrOfAscii = uI.setAsciiList()
    asciiToString(arrOfAscii)
    input("Press \"Enter\" to exit")

main()

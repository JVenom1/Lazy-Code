
# "" -> []
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

# demo data
stringToAscii("Hello World")
asciiToString([87, 111, 114, 108, 100, 32, 72, 101, 108, 108, 111])

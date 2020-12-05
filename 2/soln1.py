import re

def doCode():

    numValid = 0

    matchStr = "(\d+)-(\d+) (.): (\w+)"
    m = re.compile(matchStr)

    while True:
        try:
            i = input()
            match = m.fullmatch(i)

            minCount = int(match.group(1))
            maxCount = int(match.group(2))
            theChar = match.group(3)
            string = match.group(4)

            count = string.count(theChar)
            if minCount <= count <= maxCount:
                numValid += 1
        except EOFError as error:
            return numValid

    return numValid 

print(f"answer: {doCode()}")

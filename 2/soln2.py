import re

def doCode():

    numValid = 0

    matchStr = "(\d+)-(\d+) (.): (\w+)"
    m = re.compile(matchStr)

    while True:
        try:
            i = input()
            match = m.fullmatch(i)

            index1 = int(match.group(1)) - 1
            index2 = int(match.group(2)) - 1
            theChar = match.group(3)
            s = match.group(4)

            numValid += (s[index1] == theChar) ^ (s[index2] == theChar)

        except EOFError as error:
            return numValid

    return numValid 

print(f"answer: {doCode()}")

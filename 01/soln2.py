def doCode():
    seenOne = set()
    seenTwo = {}

    while True:
        i = eval(input())
        if i in seenTwo:
            return i * seenTwo[i] * (2020 - i - seenTwo[i])
        for n in seenOne:
            seenTwo[2020 - i - n] = n
        seenOne.add(i)

print(f"answer: {doCode()}")

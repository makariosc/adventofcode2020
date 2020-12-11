import re
from collections import Counter

def recursiveSum(outerBag, graph):
    if outerBag not in graph:
        return 0

    innerSum = 0
    innerBags = graph[outerBag]
    for b in innerBags:
        n = int(innerBags[b])
        innerSum += n + n*recursiveSum(b, graph)
    return innerSum

def doCode():

    f = open("input", "r+")
    lines = f.readlines()

    matcher = re.compile("(\d+ )?([a-z]+ [a-z]+) bag")

    # graph[outerBag] = Counter of innerBags
    graph = {}

    # construct the graph
    for l in lines:
        bags = matcher.findall(l)
        outer = bags[0][1]
        inners = bags[1:]

        if outer not in graph:
            graph[outer] = Counter()
        
        for n, b in inners:
            if n.strip() == "":
                continue
            n = int(n)
            graph[outer].update([b]*n)

    # do DFS
    return recursiveSum("shiny gold", graph)

print(f"answer: {doCode()}")

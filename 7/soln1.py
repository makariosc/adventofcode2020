import re

# This is a DFS because we recurse on each bag as we see it
def recursiveSearch(innerBag, graph, outerBags):
    if innerBag in graph:
        for outerBag in graph[innerBag]:
            # impliciltly ignore any bag we've already seen
            if outerBag not in outerBags:
                outerBags.add(outerBag)
                recursiveSearch(outerBag, graph, outerBags)
    return outerBags

def doCode():

    ret = 0
    f = open("input", "r+")
    lines = f.readlines()

    graph = {}

    matcher = re.compile("([a-z]+ [a-z]+) bag")

    # construct the directed graph in an adjacency list
    for l in lines:
        c = matcher.findall(l)
        outerBag = c[0]
        innerBags = c[1:]

        for bag in innerBags:
            if bag not in graph:
                graph[bag] = set()
            graph[bag].add(outerBag)

    # Search the graph starting at "shiny gold"
    outerBags = set()
    return len(recursiveSearch("shiny gold", graph, outerBags))

print(f"answer: {doCode()}")

import Reader


def createTree():
    bagIDs = {}
    children = {}

    for data in Reader.read("input"):
        parent, rules = data.split(" bags contain ")

        if parent not in bagIDs:
            bagIDs[parent] = len(bagIDs)

        if not rules == "no other bags.":
            newChildren = []
            for rule in rules.split(", "):
                ruleSplit = rule.split(" ")
                child = " ".join(ruleSplit[1:-1])
                if child not in bagIDs:
                    bagIDs[child] = len(bagIDs)

                childID = bagIDs[child]
                newChildren.append((childID, int(ruleSplit[0])))
            children[bagIDs[parent]] = newChildren

    return bagIDs, children


def run():
    bagIDs, children = createTree()

    rootID = bagIDs["shiny gold"]
    total = 0
    queue = children[rootID]

    while len(queue) > 0:
        current = queue.pop()
        total += current[1]

        if current[0] in children:
            newChildren = children[current[0]]
            for child in newChildren:
                queue.append((child[0], child[1]*current[1]))

    return total


print(f'Answer: {run()}')


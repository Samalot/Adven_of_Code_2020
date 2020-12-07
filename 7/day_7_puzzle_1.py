import Reader


def run():
    totalValid = 0
    bagIDs = {}
    parents = {}

    for data in Reader.read("input"):
        parent, rules = data.split(" bags contain ")

        if parent not in bagIDs:
            bagIDs[parent] = len(bagIDs)

        if not rules == "no other bags.":
            for rule in rules.split(", "):
                child = " ".join(rule.split(" ")[1:-1])
                if child not in bagIDs:
                    bagIDs[child] = len(bagIDs)

                childID = bagIDs[child]
                if childID in parents:
                    parents[childID].append(bagIDs[parent])
                else:
                    parents[childID] = [bagIDs[parent]]

    rootID = bagIDs["shiny gold"]
    seen = set(parents[rootID])
    next = set(parents[rootID])

    while len(next) > 0:
        tempSet = set()
        for id in next:
            if id in parents:
                for parent in parents[id]:
                    if parent not in seen:
                        tempSet.add(parent)
                        seen.add(parent)

        next = tempSet

    return len(seen)


print(f'Answer: {run()}')


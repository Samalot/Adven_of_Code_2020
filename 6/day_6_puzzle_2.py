import Reader


def reduceGroup(group):
    if len(group) == 1:
        return len(group[0])

    sameAnswer = group[0].intersection(group[1])
    for i in range(2, len(group)):
        sameAnswer = group[i].intersection(sameAnswer)

    return len(sameAnswer)


def run():
    currentGroup = []
    groups = []

    for data in Reader.read("input"):
        if data == "":
            groups.append(reduceGroup(currentGroup))
            currentGroup = []
        else:
            newSet = set()
            for char in data:
                newSet.add(char)
            currentGroup.append(newSet)

    groups.append(reduceGroup(currentGroup))

    return sum(groups)


print(f'Answer: {run()}')
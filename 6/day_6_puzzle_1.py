import Reader


def run():
    current = set()
    groups = []

    for data in Reader.read("input"):
        if data == "":
            groups.append(len(current))
            current = set()
        else:
            for char in data:
                current.add(char)
    groups.append(len(current))

    return sum(groups)


print(f'Answer: {run()}')
import Reader


def countTree(right, down):
    map = []
    for data in Reader.read("input"):
        map.append(data)

    total = 0
    onSlope = True
    posX, posY = 0, 0

    while onSlope:
        posX = (posX + right) % len(map[0])
        posY += down

        onSlope = posY < len(map)

        if onSlope and map[posY][posX] == "#":
            total += 1

    return total


def run():
    total = 1

    for count in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        total *= countTree(count[0], count[1])

    return total


print(f'Answer: {run()}')
import Reader


def run():
    map = []
    for data in Reader.read("input"):
        map.append(data)

    total = 0
    onSlope = True
    posX, posY = 0, 0

    while onSlope:
        posX = (posX + 3) % len(map[0])
        posY += 1

        onSlope = posY < len(map)

        if onSlope and map[posY][posX] == "#":
            total += 1

    return total


print(f'Answer: {run()}')
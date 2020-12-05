import Reader


def run():
    highest = 0

    for data in Reader.read("input"):

        lower, upper = 0, 127
        for i in range(7):
            h = (upper - lower)//2
            if data[i] == "F":
                upper = lower + h
            elif data[i] == "B":
                lower = upper - h

        left, right = 0, 7
        for i in range(7, 10):
            h = (right - left) // 2
            if data[i] == "L":
                right = left + h
            elif data[i] == "R":
                left = right - h

        highest = max(highest, (lower * 8) + left)

    return highest


print(f'Answer: {run()}')
import Reader


def run():
    data = []
    for number in Reader.read("input"):
        data.append(int(number))

    data = sorted(data)

    totalDiff = [0, 0, 0, 1]
    totalDiff[data[0]] += 1
    for i in range(1, len(data)):
        totalDiff[(data[i] - data[i-1])] += 1

    return totalDiff[1] * (totalDiff[3])


print(f'Answer: {run()}')


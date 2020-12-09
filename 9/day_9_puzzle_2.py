import Reader


def run():
    target = 50047984

    data = []
    for number in Reader.read("input"):
        data.append(int(number))

    sums = set()
    for i in range(len(data)):
        if (target - data[i]) in sums:
            group, sum = [], 0
            for j in range(i):
                group.append(data[i-j])
                sum += data[i-j]
                if sum == target:
                    return min(group) + max(group)

        else:
            newSums = set()
            for number in sums:
                newSums.add(number + data[i])
            newSums.add(data[i])
            sums = newSums

    return "Invalid"


print(f'Answer: {run()}')


import Reader
from collections import deque


def run():
    preamble = 25

    data = []
    for number in Reader.read("input"):
        data.append(int(number))

    sums = deque([set() for i in range(preamble-1)])
    for i in range(preamble):
        for j in range(i+1, preamble):
            sums[i].add(data[i]+data[j])

    for i in range(preamble, len(data)):
        if any(data[i] in s for s in sums):
            sums.popleft()
            sums.append(set())
            for j in range(preamble-1):
                index = i - ((preamble-1)-j)
                sums[j].add(data[index] + data[i])
        else:
            return data[i]

    return -1


print(f'Answer: {run()}')


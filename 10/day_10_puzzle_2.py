import Reader

memo = {0: 1}


def trace(index, num, data):
    if num in memo:
        return memo[num]

    r = 3
    if index < 3:
        r = index

    total = 0
    for i in range(1, r+1):
        if num - data[index - i] <= 3:
            total += trace(index - i,  data[index - i], data)

    memo[num] = total
    return total


def run():
    data = [0]
    for number in Reader.read("input"):
        data.append(int(number))

    data = sorted(data)
    target = data[-1] + 3

    return trace(len(data), target, data)


print(f'Answer: {run()}')


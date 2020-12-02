import Reader


def run():
    numbers = []
    seen = set()

    for data in Reader.read("input"):
        x = int(data)
        numbers.append(x)

    combo = {}
    for i in range(len(numbers)-1):
        for j in range(i, len(numbers)):
            x = numbers[i]+numbers[j]
            if x <= 2020:
                combo[x] = [i, j]

    for i in range(len(numbers)):
        c = 2020 - numbers[i]
        if c in combo:
            print(numbers[i] * numbers[combo[c][0]] * numbers[combo[c][1]])
            return


print(f'Answer: {run()}')


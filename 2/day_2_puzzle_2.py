import Reader


def run():
    totalValid = 0

    for data in Reader.read("input"):
        policy, password = data.split(": ")
        indexes, char = policy.split(" ")
        a, b = [int(n)-1 for n in indexes.split("-")]

        x = (password[a] == char)
        y = (password[b] == char)

        if (x or y) and not (x and y):
            totalValid += 1

    return totalValid


print(f'Answer: {run()}')
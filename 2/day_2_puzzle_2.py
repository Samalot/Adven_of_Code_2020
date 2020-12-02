import Reader


def run():
    totalValid = 0

    for data in Reader.read("input"):
        s = data.split(": ")

        a = int(s[0].split(" ")[0].split("-")[0]) - 1
        b = int(s[0].split(" ")[0].split("-")[1]) - 1
        char = s[0].split(" ")[1]

        if (s[1][a] == char or s[1][b] == char) and not (s[1][a] == char and s[1][b] == char):
            totalValid += 1

    return totalValid


print(f'Answer: {run()}')

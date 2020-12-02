import Reader


def run():
    totalValid = 0

    for data in Reader.read("input"):
        s = data.split(": ")

        minCount = int(s[0].split(" ")[0].split("-")[0])
        maxCount = int(s[0].split(" ")[0].split("-")[1])
        charCount = s[0].split(" ")[1]

        count = 0
        for char in s[1]:
            if char == charCount:
                count += 1

        if count >= minCount and count <= maxCount:
            totalValid += 1

    return totalValid


print(f'Answer: {run()}')


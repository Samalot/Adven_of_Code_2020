import Reader


def run():
    totalValid = 0

    for data in Reader.read("input"):
        policy, password = data.split(": ")
        policy, c = policy.split(" ")

        minCount = int(policy.split("-")[0])
        maxCount = int(policy.split("-")[1])

        count = 0
        for char in password:
            if char == c:
                count += 1
                if count > maxCount:
                    break

        if maxCount >= count >= minCount:
            totalValid += 1

    return totalValid


print(f'Answer: {run()}')


import Reader


def run():
    seen = set()

    for data in Reader.read("input"):
        seen.add(2020 - int(data))

    for data in Reader.read("input"):
        if int(data) in seen:
            x = int(data)
            return x * (2020-x)


print(f'Answer: {run()}')

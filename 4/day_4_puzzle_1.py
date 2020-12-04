import Reader


def generatePassports():
    current = {}
    for data in Reader.read("input"):
        if data == "":
            yield current
            current = {}
        else:
            for pair in data.split(" "):
                key, value = pair.split(":")
                current[key] = pair
    yield current


def run():
    valid = 0
    check = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for passport in generatePassports():
        if all([code in passport for code in check]):
            valid += 1

    return valid


print(f'Answer: {run()}')
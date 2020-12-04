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
                current[key] = value
    yield current


def rangeValidate(minVal, maxVal, val):
    return maxVal >= int(val) >= minVal


def heightValidate(val):
    if "cm" in val:
        return rangeValidate(150, 193, val.split("cm")[0])
    if "in" in val:
        return rangeValidate(59, 76, val.split("in")[0])
    return False


def run():
    valid = 0
    hexDigits = "0123456789abcdefABCDEF"
    policy = {
        "byr": lambda v: v and rangeValidate(minVal=1920, maxVal=2002, val=v),
        "iyr": lambda v: v and rangeValidate(minVal=2010, maxVal=2020, val=v),
        "eyr": lambda v: v and rangeValidate(minVal=2020, maxVal=2030, val=v),
        "hgt": lambda v: v and heightValidate(val=v),
        "ecl": lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda v: v and len(v) == 9 and v.isnumeric(),
        "hcl": lambda v: v and v[0] == "#" and all([v[i] in hexDigits for i in range(1, len(v))]),
    }

    for passport in generatePassports():
        if all([policy[check](passport.get(check, False)) for check in policy.keys()]):
            valid += 1

    return valid


print(f'Answer: {run()}')
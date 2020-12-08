import Reader


def accumulate(pointer, accumulator, val):
    accumulator += int(val)
    pointer += 1
    return pointer, accumulator


def jump(pointer, accumulator, val):
    pointer += int(val)

    return pointer, accumulator


def run():
    pointer = 0
    accumulator = 0
    instructions = {
        "acc": lambda v: v and accumulate(pointer, accumulator, val=v),
        "jmp": lambda v: v and jump(pointer, accumulator, val=v),
        "nop": lambda v: v and accumulate(pointer, accumulator, val=0)
    }
    seen = set()

    program = []
    for data in Reader.read("input"):
        program.append(data.split(" "))

    while (pointer not in seen) and (pointer < len(program)):
        code, value = program[pointer]
        seen.add(pointer)
        test = instructions[code](value)
        pointer, accumulator = test

    return accumulator


print(f'Answer: {run()}')


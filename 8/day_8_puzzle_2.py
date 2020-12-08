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
    candidates = []

    program = []
    for data in Reader.read("input"):
        program.append(data.split(" "))

    memo = [1 for i in range(len(program)+1)]
    while (memo[pointer] == 1) and (pointer < len(program)):
        code, value = program[pointer]

        if not code == "acc":
            candidates.append([pointer, accumulator])

        memo[pointer] = 0
        pointer, accumulator = instructions[code](value)

    for candidate in candidates:
        pointer, accumulator = candidate
        memo[pointer] = 1

        program[pointer][0] = "jmp" if (program[pointer][0] == "nop") else "nop"

        while (memo[pointer] == 1) and (pointer < len(program)):

            code, value = program[pointer]
            memo[pointer] = 0
            pointer, accumulator = instructions[code](value)

            if pointer >= len(program):
                return accumulator

        program[pointer][0] = "jmp" if (program[pointer][0] == "nop") else "nop"

    return "Error"


print(f'Answer: {run()}')


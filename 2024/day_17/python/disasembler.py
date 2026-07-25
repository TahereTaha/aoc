import sys

def disasemble_opcode(opcode):
    if (opcode == 0):
        return "adv"
    if (opcode == 1):
        return "bxl"
    if (opcode == 2):
        return "bst"
    if (opcode == 3):
        return "jnz"
    if (opcode == 4):
        return "bxc"
    if (opcode == 5):
        return "out"
    if (opcode == 6):
        return "bdv"
    if (opcode == 7):
        return "cdv"
    return "unknown_instruction"

def disasemble_operand(opcode, operand):
    if (opcode == 0 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7):
        if (operand <= 3):
            return "\x1b[0;36m"+ str(operand) + "\x1b[0m"
        if (operand == 4):
            return "\x1b[0;36m"+ "reg_a" + "\x1b[0m"
        if (operand == 5):
            return "\x1b[0;36m"+ "reg_b" + "\x1b[0m"
        if (operand == 6):
            return "\x1b[0;36m"+ "reg_c" + "\x1b[0m"
    return str(operand)

def disasemble_instruction(opcode, operand):
    return disasemble_opcode(opcode) + " " + disasemble_operand(opcode, operand)

if (len(sys.argv) >= 2 and sys.argv[1] == "test"):
    file = open("test_input", "r")
else:
    file = open("input", "r")
content = file.read()[:-1]
file.close()

register_a = int(content.split("\n")[0].split(":")[1])
register_b = int(content.split("\n")[1].split(":")[1])
register_c = int(content.split("\n")[2].split(":")[1])

program = [int(x) for x in content.split("\n")[4].split(":")[1].split(",")]

print()
print("machine state:")
print("\treg_a: ", register_a)
print("\treg_b: ", register_b)
print("\treg_c: ", register_c)
print()
print("program: ", program)
print()
print("disasembled code")

for i in range(len(program) // 2):
    print("\t", str(i) + ":", program[i * 2], program[i * 2 + 1], "\t", disasemble_instruction(program[i * 2], program[i * 2 + 1]))


print("0:")
for i in range(16):
    print("\t" + bin(i), "\t:" + str(i), "->", (((i & 0b1) ^ (i // (2 ** (i & 0b1)))) ^ 0b110) & 0b111)


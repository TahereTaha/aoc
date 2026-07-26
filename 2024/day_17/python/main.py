import sys
from Computer import *

if (len(sys.argv) >= 2 and sys.argv[1] == "test"):
    file = open("test_input", "r")
else:
    file = open("input", "r")
content = file.read()[:-1]
file.close()

reg_a = int(content.split("\n")[0].split(":")[1])
reg_b = int(content.split("\n")[1].split(":")[1])
reg_c = int(content.split("\n")[2].split(":")[1])

program = [int(x) for x in content.split("\n")[4].split(":")[1].split(",")]

computer = Computer(reg_a, reg_b, reg_c, program)

answer1 = computer.get_output()

print("the first answer is:", answer1)

answer2 = 7

def list_equal(list1, list2):
    if (len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if (list1[i] != list2[i]):
            return False
    return True


def search_answer2(reg_a):
    computer = Computer(reg_a, 0, 0, program)
    output = computer.get_output()
    if (list_equal(program, output)):
        return reg_a
    if (len(output) >= len(program)):
        return 0
    for i in range(8):
        computer = Computer(reg_a * 8 + i, 0, 0, program)
        output = computer.get_output()
        if (output[0] == program[len(program) - len(output)]):
            new_reg_a = search_answer2(reg_a * 8 + i)
            if (new_reg_a != 0):
                return new_reg_a
    return 0

answer2 = search_answer2(answer2)

computer = Computer(answer2, 0, 0, program)
print("confinmation:", program)
print("confinmation:", computer.get_output())

print("the second answer is:", answer2)

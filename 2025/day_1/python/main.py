import sys

def dial_update(dial, instruction):
    direction = instruction[:1]
    magnitude = int(instruction[1:]) % 100
    if (direction == "L" and dial < magnitude):
        dial = dial + 100 - magnitude
    elif (direction == "R" and 99 < dial + magnitude):
        dial = dial - 100 + magnitude
    elif (direction == "R"):
        dial = dial + magnitude
    elif (direction == "L"):
        dial = dial - magnitude
    else:
        dial = dial
    return dial

def overflow_count(dial, instruction):
    count = int(instruction[1:]) // 100
    direction = instruction[:1]
    magnitude = int(instruction[1:]) % 100
    if (direction == "L" and dial <= magnitude and dial != 0):
        count = count + 1
    elif (direction == "R" and dial + magnitude >= 100):
        count = count + 1
    return count

if (len(sys.argv) >= 2 and sys.argv[1] == "test"):
    file = open("test_input", "r")
else:
    file = open("input", "r")
content = file.read()[:-1]
file.close()


instructions = content.split("\n")

dial_position = 50

answer1 = 0
answer2 = 0

for instruction in instructions:
    answer2 = answer2 + overflow_count(dial_position, instruction)
    dial_position = dial_update(dial_position, instruction)
    if (dial_position == 0):
        answer1 = answer1  + 1

print("the answere to the first part is: ", answer1)
print("the answere to the second part is: ", answer2)




import sys

if (len(sys.argv) >= 2 and sys.argv[1] == "test"):
    file = open("test_input", "r")
else:
    file = open("input", "r")
content = file.read()[:-1]
file.close()

print(content)


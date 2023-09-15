import numpy as np

fileName = "test.txt"
data = np.loadtxt(fileName, str)


with open(fileName, 'r') as file:
    lines = file.readlines()


result = []
for i in range(0, len(data), 1):
    result.append(data[i][1].split(","))
    #print(result)
    i = i + 1

print("i equals ",i)
for k in range(0, len(result), 1):
    for j in range(0, len(result[k]), 1):
        
        if result[k][j] == '"NULL':
            deletedLines = lines.pop(result[k])
            k = k + 1
            j = 0


i = 0
for i in range(len(lines)):
    with open("cleanfile.txt", "w") as file:
        file.write(lines[i])
        print("wrote to the file")
        i = i + 1


# if result[1] == '"NULL"':
#     print("null!!!")
# else:
#     print("oh well")
# print(result[1])
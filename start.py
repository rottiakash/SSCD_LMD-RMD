import re

rules = {}
res = []


def LMD(sentinel):
    if len(sentinel) > strLen:
        return "dead"

    if sentinel == string:
        return "Done"
    else:
        index = 0
        try:
            while not sentinel[index].isupper():
                index += 1
        except:
            return "dead"
        temp = str(sentinel)
        for i in rules.keys():
            if temp[index] == i:
                for j in rules[i]:
                    if j == "@":
                        temp = str(sentinel[:index] + sentinel[index + 1 :])
                    else:
                        temp = str(sentinel[:index] + j + sentinel[index + 1 :])
                    if len(temp) > strLen:
                        continue

                    if LMD(temp) == "Done":
                        if j == "@":
                            res.append([i, ""])
                        else:
                            res.append([i, j])
                        return "Done"
                    else:
                        continue
        return "dead"


def RMD(sentinel):
    if len(sentinel) > strLen:
        return "dead"

    if sentinel == rmdString:
        return "Done"
    else:
        index = len(sentinel) - 1
        try:
            while not sentinel[index].isupper():
                index -= 1
                if index < 0:
                    return "dead"
        except:
            return "dead"
        temp = str(sentinel)
        for i in rules.keys():
            if temp[index] == i:
                for j in rules[i]:
                    if j == "@":
                        temp = str(sentinel[:index] + sentinel[index + 1 :])
                    else:
                        temp = str(sentinel[:index] + j + sentinel[index + 1 :])
                    if len(temp) > strLen:
                        continue
                    if RMD(temp) == "Done":
                        if j == "@":
                            res.append([i, ""])
                        else:
                            res.append([i, j])
                        return "Done"
                    else:
                        continue
        return "dead"


print("Enter the productions(Use @ for Epsilon):")

for i in input().split(" "):
    RHS = []
    NT = ""
    rule = re.split("->|\|", i)
    length = len(rule)
    for index, j in enumerate(rule):
        if index == 0:
            NT = j
            continue
        RHS.append(j)
        if index == length - 1:
            rules[NT] = RHS

string = input("Enter the input string:")
start = input("Enter the start symbol:")
print()
print()
rmdString = str(string)
rmdStart = str(start)
strLen = len(string)

for i in rules.keys():
    for j in rules[i]:
        if j == "@":
            strLen += 15
            break
LMD(start)
res.reverse()
print("LMD is:")
print(start + "=>", end=" ")
length = len(res)
for index, i in enumerate(res):
    start = start.replace(i[0], i[1], 1)
    print(start)
    if not index == length - 1:
        print("=>", end=" ")
res.clear()
RMD(rmdStart)
res.reverse()
print()
print()
print("RMD is:")
print(rmdStart + "=>", end=" ")
length = len(res)
for index, i in enumerate(res):
    rmdStart = i[1].join(rmdStart.rsplit(i[0], 1))
    print(rmdStart)
    if not index == length - 1:
        print("=>", end=" ")

print()
print()
input("Press any key to continue")

print("Введите элементы списка:")
trueArray = []
numArray = []
elseArray = []
numPlenty = set()
elseDict = dict()
tNum = 0

while(1):
    tempStr = input()

    if tempStr == "":
        break
    if tempStr.isspace():
        continue

    if tempStr.isnumeric():
        numPlenty.add(int(tempStr))
        numArray.append(tempStr)
        continue

    tempArray = tempStr.split()

    if tempStr.isupper() or tempStr.find('F') == -1 or tempArray[0].isupper() or not tempStr.isalnum():
        tempMeaning = "error_"
        tempMeaning += str(tNum)
        tNum += 1
        x = {f'{tempStr}': f'{tempMeaning}'}
        elseDict.update(x)
        elseArray.append(tempStr)
    else:
        trueArray.append(tempStr)

print("Подходящие элементы:")
for x in trueArray:
    print(x)
print("Числа:")
for x in numArray:
    print(x)


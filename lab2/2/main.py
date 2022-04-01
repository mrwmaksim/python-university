import math
import string


def checkString(string="max"):
    if string == "":
        print("Ошибка")
        return False
    else:
        return True


string = input("Введите строку: ")
array = string.split()

numArray = []
strArray = []

if not checkString(string):
    quit()

for element in array:
    if element == " ":
        continue

    if element.isnumeric() == True:
        numArray.append(int(element))
    else:
        strArray.append([element,len(element)])

if len(numArray) != 0:
    sumNum = 0
    print ("Целочисленные элементы:")
    for element in numArray:
        print(element)
        sumNum += element
    print("Сумма равна:", sumNum)
else:
    print("Чисел нет")

if len(strArray) != 0:
    i = 0
    n = len(strArray) - 1
    for i in range(0, n):
        for j in range (0, n):
            if strArray[j][1] > strArray[j+1][1]:
                strArray[j], strArray[j+1] = strArray[j+1], strArray[j]

    strString = ""
    for i in range(0, len(strArray)):
        strString += strArray[i][0]
        strString += " "

    print("Строка: ", strString)

else:
    print("Слов в строке нет")




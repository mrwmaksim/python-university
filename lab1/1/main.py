import math

def check(n="1"):
    try:
        float(n)
        return True
    except ValueError:
        print("Ошибка ввода")
        return False


print("Введите данные: ")
a = input('a = ')
b = input('b = ')
c = input('c = ')
k = input('k = ')

a = int(a)
b = int(b)
c = int(c)
k = int(k)

if not check(a) or not check(b) or not check(c) or not check(k):
    exit()

if ((b-c) < 0 or c < 0):
    print("Ошибка ввода")
    exit()
sum = (a*5) + math.pow(b-c, 0.5) + (k/c)*(math.pow(a,3) + math.pow(b,2)-math.pow(c,3))
print (sum)

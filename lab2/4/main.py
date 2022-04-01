import math
def check(a = "1"):
    if not a.isalnum() or int(a) <= 0:
        return False
    else:
        return True

def square(a = 1):
    a = float(a)
    per = a*4
    square = a*a
    diagonalSquare = a*a + a*a
    diagonal = pow(diagonalSquare, 0.5)
    korteg = ()
    korteg = (per, square, diagonal)
    return korteg

a = input("Введите сторону квадрата:")
if not check(a):
    print("Ошибка")
    exit()

korteg=()
korteg = square(a)

print("Периметр равен \t\t%.3f\nПлощадь равна \t\t%.3f\nДиагональ равна \t%.3f\n" % (korteg[0], korteg[1], korteg[2]))





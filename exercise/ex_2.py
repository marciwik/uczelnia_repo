import math

# trojkat

a = 40
b = 12
c = 8
h = 6
pole = 1/2 * a * h
obwod = a + b + c

print("Pole trojkata wynosi " + str(pole) + ", a obwód trojkata wynosi " + str(obwod) + ".")

# romb

a = 5
h = 3

pole = a * h
obwod = 4 * a

print("Pole rombu wynosi " + str(pole) + ", a obwód rombu wynosi " + str(obwod) + ".")

# koło

r = 7
math.pi

pole = math.pi * r ** 2
obwod = 2 * math.pi * r

print("Pole koła wynosi " + str(pole) + ", a obwód koła wynosi " + str(obwod) + ".")

# kwadrat

a = 9

pole = a * a
obwod = 4 * a

print("Pole kwadratu wynosi " + str(pole) + ", a obwód kwadratu wynosi " + str(obwod) + ".")

# trapez

a = 12
b = 7
c = 10
d = 9
h = 8

pole = ((a + b) * h ) / 2
obwod = a + b + c + d

print("Pole trapezu wynosi " + str(pole) + ", a obwód trapez wynosi " + str(obwod) + ".")
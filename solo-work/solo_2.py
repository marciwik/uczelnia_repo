import math

# trójkąt

def trojkat(bok_a, bok_b, bok_c, h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod 
    
print(f'Pole i obwód trójkąta wynoszą: {trojkat(10,15,12,8)}')

# koło

def kolo(promien, pi):
    pole = pi * promien**2
    obwod = 2 * pi * promien
    return pole, obwod

print(f'Pole i obwód koła wynoszą: {kolo(6,math.pi)}')

# trapez

def trapez(bok_a, bok_b, bok_c, h_a):
    pole = 1/2 * (bok_a + bok_b) * h_a
    obwod = bok_a + bok_b + 2 * bok_c
    return pole, obwod

print(f'Pole i obwód trapezu wynoszą: {trapez(10, 8, 6, 3)}')
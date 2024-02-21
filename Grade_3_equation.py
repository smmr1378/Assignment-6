import math
print("the Grade 3 equation form is : ax^3 + bx^2 + cx + d")

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))
d = int(input('enter d: '))


delta = (18 * a * b * c) - (4 * (b**3) * d) + ((b**2)*(c**2)) - (4 * a * (c**3)) - (27 * (a**2) * (d**2))

delta0 = (b**2) - (3 * a * c)
delta1 = (2 * (b**3)) - (9 * a * b * c) + (27 * (a**2) * d)
delta2 = (-27 * (a**2) * delta)

C = ((delta1 + math.sqrt(delta2)) / 2) ** (1. / 3)

z = complex(-1 , math.sqrt(3))
u1 = 1
u2 = z / 2
u3 = (z.conjugate()) / 2

x1 = (-1 /(3 * a)) * (b + (u1 * C) + ((delta0) / (u1 * C)))
x2 = (-1 /(3 * a)) * (b + (u2 * C) + ((delta0) / (u2 * C)))
x3 = (-1 /(3 * a)) * (b + (u3 * C) + ((delta0) / (u3 * C))) 

print ("x1: ", x1)
print ("x2: ", x2)
print ("x3: ", x3)
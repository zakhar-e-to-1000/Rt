from math import cos, log
x=1.155
y=3.981
result = log(x**2 + 4*x*y + y**2) \
         - 12*cos(x*y**4) + 13*x**6
print(round(result, 4))

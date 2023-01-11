"""
                Bienvenido al día 12 de #100diasdepython
                        El reto de hoy es:
Intercambia los valores de dos variables e imprime su ubicación en memoria
                        utilizando la función id()
"""
a,b=100,200
print("a=",a,id(a))
print("b=",b,id(b))
a,b=b,a
print("a=",a,id(a))
print("b=",b,id(b))
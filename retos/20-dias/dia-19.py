"""
        Bienvenido al día 19 de #100diasdepython
                El reto de hoy es:
Declara una variable de tipo cadena, reviértela sin usar 
    funciones adicionales e imprime el resultado.
"""
x,r = 'Mandarina', ''
for i in range(0,len(x)):
    r = x[i] + r
print(r)
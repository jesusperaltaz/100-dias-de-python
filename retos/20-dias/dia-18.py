"""
                Bienvenido al día 18 de #100diasdepython
                        El reto de hoy es:
Declara una variable de tipo cadena, encuentra el primer y último carácter
                en orden lexicográfico sin usar ciclos e imprímelos.
"""
text='pythonista'
orden=sorted(text)
print(f"Primer caracter:",orden[0],"Ultimo caracter:",orden[-1])
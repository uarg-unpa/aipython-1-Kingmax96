# 13. Escribir un programa que calcule el promedio de precios de 10 productos.
def suma_de_productos(count:int):

    productos  = []
    total = 0 

    for producto in range(count):
        productos.append(float(input(f'ingrese valor producto {producto +1}: ')))
        

    total = sum(productos)    
    return(f'''los valores de los productos son de: 
        {productos}
    y  la suma de éstos es igual a: {total}''')


print(suma_de_productos(10))


    

#ver como sumar todos los valores de una lista.

# resultado = productos/10
# print(resultado)
#ejercicio 6
#crear un programa que solicite 2 numeros enteros, luego realizar:
print('en el siguiente programa, pediremos 2 numeros enteros y realizaremos las siguientes operaciones:')
print('suma, resta, producto, potencia y tambien calcularemos su resto.')
#peticion de valores
num1 = int(input('ingrese primer numero'))
num2 = int(input('ingrese segundo numero'))
#resultados
res_suma = num1+num2
res_dif = num1-num2
res_prod = num1*num2
res_pot = num1**num2
res_res = num1%num2
#imprime resultados.-
print(f"""
Los resultados de las operaciones son los siguientes:
a. suma = {res_suma}
b. resta = {res_dif}
c. producto = {res_prod}
d. potencia = {res_pot}
e. resto = {res_res}
      """)
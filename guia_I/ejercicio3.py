# 3. Definir nombres variables representativos para las siguientes características:
# a. tu nombre
name = 'max'
# b. tu apellido
last_name = 'king'
# c. tu edad
age = 27
# d. tu altura
height = 1.69
# e. un número de vuelo
fly_number = 1101
# f. La temperatura del ambiente
temperature = 28 
# g. El salario mensual
salary = 2000000
# h. Para representar que el juego termino
game = 0

# i. Para determinar si un número es par
def numero_par(numero):
    if (numero%2==0):
        print(f'el numero ingresado es par')
    else:
        print(f'el numero ingresado no es par')
numero_par(20)
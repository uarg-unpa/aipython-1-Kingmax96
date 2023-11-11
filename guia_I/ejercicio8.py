# Se desea conocer el perímetro y el área de un rectángulo según su base y altura. Así
# mismo también se desean conocer los mismos datos para una circunferencia según
# su radio

#dudas que hago con pi ? (3,14)
pi = 3.14
r = float(input(f'ingrese el valor del radio de la circunferencia para concoer su perimetro'))

res_perimetro = (pi*(r**2))
print(f'el perimetro es: {res_perimetro}')

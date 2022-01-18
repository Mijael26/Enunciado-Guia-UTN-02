# Se tiene información del legajo y la nota obtenida por 40 alumnos. Se solicita informar:
# a)	Cuántos alumnos sacaron notas mayores al promedio. 
# b)	Informar los legajos de los alumnos que no aprobaron (nota menor a 4).



nota = [0] * (5)
legajo = [0] * (5)

sum = 0
pRO = 0
cont = 0
for h in range(0, 5, 1):
    nota[h] = int(input("Ingrese nota : "))
    legajo[h] = int(input("Ingrese Legajo : "))
    sum = sum + nota[h]

pRO = float(sum) / 5

for h in range(0, 5, 1):
    if pRO >= nota[h]:
        cont = cont + 1

print("Los legajos con notas mayores que 4  : ")
for h in range (0,5,1) :
    if nota[h]>4 :
        print(legajo[h])

print(f"Cuantos sacaron mas que el promedio : {cont}")


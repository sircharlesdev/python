print("Programa de Becas 2020")
distancia_escuela=int(input("Introduce distancia a la escuela"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el número de hermanos"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual"))
print(salario_familiar)


if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")

else:
    print("No te corresponde beca")
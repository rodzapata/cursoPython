familia=["rodney","cecilia","juan miguel","samuel"]
print(familia)

familia[3]="Samuel david"
print(familia)

familia.append("elkin jose")
print(familia)

familia[-1]="angelica"
print(familia)

familia[0]="jesus"
print(familia)

familia.insert(0,"adriam")
print(familia)

#eliminamos de la lita a Rodney
familia.remove("angelica")
print(familia)

#eliminamos al ultimo de la lista
familia.pop()
print(familia)

#ordenamos
familia.sort()
print(familia)

#recorrer la lista a travez de un ciclo
print("---ciclor for de un alista")
for nombre in familia:
    print(nombre)

#copiar familia
print("----creando copia de lista -----")
familia2=familia.copy()
print(familia2)

#sublisa
print("----creando copia de lista -----")
subfamilia=familia[1:3]
print(subfamilia)



listFrutas=["uva","pera","manzana","banana"]
print(listFrutas)
listFrutas.append("naranja")
print(listFrutas)

#condicinarl
if "pera" in listFrutas:
    listFrutas.remove("pera")

print(listFrutas)
print("--ciclo for")
for fruta in listFrutas:
    print(fruta)
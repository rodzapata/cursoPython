#listas pemite valores duplicados
numero=[1,2,3,4,5,4,2]
print(numero)

#conjunto Set no permite valores duplicados, como el 3 esta 2 veces solo deja uno
numero2={1,2,3,3,4}
print(numero2)

print("--convertirmos una List a un Set de Coleccion elimandose los valores repetidos")
valoresUnicos=set(numero)
print(valoresUnicos)

#tupla valores costantes que no se puede modificar 
cordenada=(10,20)

#dicionario
print("--diccinarios ")
persona={"nombre": "rodney", "edad":50}
print(persona)
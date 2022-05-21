#Pilas (stack)
#En python trabajamos con las pilas aunque no directamente, podemos simularla con una lista.
#LIFO LAST IN FIRST OUT
pila = [1,2,3]

#Agregamos elementos por el final de la pila
pila.append(4)

print (pila)
#Sacar elementos de una pila, el último que entró, primero en salir

elemento_final = pila.pop()

print(elemento_final)

print(pila)
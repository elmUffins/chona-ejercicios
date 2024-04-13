# Ejercicios con Chona

### Alumno: Eric Gerzenstein

### Curso: 4B TIC

## Ejercicios de la Guía - Funciones

### Ejercicio 1
```python
q = int(input("¿Cuántos números desea ingresar? "))
lista: list[int] = []
for i in range(q):
    lista.append(int(input(f"Ingrese un número: ")))

print(f"Su lista es: {lista}")
for i in lista:
    if i % 2 == 0 and i != 0:
        print(f"El número {i} es par.")
```
### Ejercicio 2
```python
q = int(input("¿Cuántos números desea ingresar? "))
lista: list[int] = []
for i in range(q):
    lista.append(int(input(f"Ingrese un número: ")))

if lista != []:
    print("El número mayor es:", max(lista))
else:
    print("No hay números en la lista.")
```
### Ejercicio 3
```python
q = int(input("¿Cuántos números desea ingresar? "))
lista: list[int] = []
for i in range(q):
    lista.append(int(input(f"Ingrese un número: ")))

if lista != []:
    print("El número menor es:", min(lista))
else:
    print("No hay números en la lista.")
```
### Ejercicio 4
```python
q = int(input("¿Cuántos números desea ingresar? "))
lista: list[int] = []
for i in range(q):
    lista.append(int(input(f"Ingrese un número: ")))

total = 0
for i in lista:
    total += i

if lista != []:
    print(f"El promedio de los números ingresados es: {total / q}")
else:
    print("No hay números en la lista.")
```
### Ejercicio 5
```python
q = int(input("¿Cuántos números desea ingresar? "))
lista: list[int] = []
for i in range(q):
    lista.append(int(input(f"Ingrese un número: ")))

nums: list[int] = []

for i in lista:
    divisible = False
    for x in lista:
        if i % x == 0 and i != x:
            divisible = True
            break
        else:
            nums.append(i)
    if not divisible:
        nums.append(i)

if len(nums) == 0 and len(lista) > 1:
    print("No hay ningún número que cumpla la condición.")
elif len(nums) == 0 and len(lista) == 1:
    print(f"Solo se ha ingresado el número {lista[0]}.")
elif len(lista) == 0:
    print("0")
else:
    print(max(nums))
```
### Ejercicio 6
```python
lista: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nlista = [i for sublista in lista for i in sublista]
print(nlista)
```
### Ejercicio 7
```python
lista: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nlista = [max(sublista) for sublista in lista]
print(nlista)
```
### Ejercicio 8
```python
def es_vocal(letra):
    if ord(letra) == 97 or ord(letra) == 101 or ord(letra) == 105 or ord(letra) == 111 or ord(letra) == 117:
        return True
    else:
        return False

print(es_vocal(input("Ingrese una letra para averiguar si es o no vocal: ").lower()))
```
### Ejercicio 9
```python
def no_vocales(char):
    if ord(char) in [97, 101, 105, 111, 117, 65, 69, 73, 79, 85]:
        return ''
    else:
        return char

string = input("Ingrese un string para eliminar las vocales: ")
result = ''.join(map(no_vocales, string))
print(list(result))
```
### Ejercicio 10
```python
lista: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
nlista: list[list[int]] = [[], []]
for i in range(len(lista)):
    for x in range(len(lista[i])):
        nlista[x].append(lista[i][x])

print(nlista)
```
## Ejercicios de la Guía - Archivos

### Ejercicio 11 - A
```python
import pandas as pd

pd.set_option('display.max_rows', None)

filename = 'usuarios.csv'
data = pd.read_csv(filename)
names = data['name']
print(names)
```
### Ejercicio 11 - B
```python
import pandas as pd

pd.set_option('display.max_rows', None)
filename = 'usuarios.csv'
data = pd.read_csv(filename)

average = (data['age'].sum() / data['age'].count())
above_average = data["age"] < average

print(data[above_average]['name'])
print(average)
```
### Ejercicio 11 - C
```python
import pandas as pd

pd.set_option('display.max_rows', None)
filename = 'usuarios.csv'
data = pd.read_csv(filename)

average = (data['age'].sum() / data['age'].count())
above_average = data["age"] < average

print(f"La edad promedio es de {average}")
```
### Ejercicio 11 - D
```python

```
### Ejercicio 11 - E
```python

```
### Ejercicio 12
```python

```
### Ejercicio 13
```python

```
### Ejercicio 14
```python

```
### Ejercicio 15
```python

```
### Ejercicio 16
```python

```
### Ejercicio 17
```python

```
### Ejercicio 18
```python

```
### Ejercicio 19
```python

```
### Ejercicio 20
```python

```

## Ejercicios en Clase

### Ejercicio 1:
```python
#Dado un nombre, responde cuantos caracteres tiene
name:str = input("Ingrese su nombre: ")
print(f"Su nombre tiene {len(name)} caracteres.")

```
### Ejercicio 2:
```python
#Dado los números enteros l, k y n, mostrar por pantalla todos los números
#divisibles por n en un rango de l hasta k
l:int = int(input("Ingrese su primer variable: "))
k:int = int(input("Ingrese su segunda variable: "))
n:int = int(input("Ingrese su divisor: "))

i:int
for i in range(l, k + 1):
    if i % n == 0:
        print(f"{i} es divisible por {n}.")
```

### Ejercicio 3: A
```python
#Dada una lista lis = [1, 2, 3, 4, 5]
#crear una nueva lista que por cada
#elemento x de lis, tenga x^2 en la lista nueva
lis: list[int] = [1, 2, 3, 4, 5]
lisC: list[int] = []
for i in lis:
    lisC.append(i**2)
print(lisC)
```
### Ejercicio 3: B
```python
#Hacer lo mismo pero en 3 listas dentro de una lista
lis: list[int] = [
    [1, 2, 3],
    [4, 5 ,6],
    [7, 8, 9]]
lisC: list[int] = [[], [], []]
for lista in lis:
    for i in lista:
        lisC[lis.index(lista)].append(i**2)
print(lisC)
```


### batalla naval todo choto
```python
N = int(input("Ingrese el tamaño deseado del tablero: "))

tablero: list[list[bool]] = \
    [

    ]

for i in range (0, N):
    espacio = []
    tablero.append(espacio)
    
print(tablero)


```

# Ejercicios con Chona
### Ejercicio en clase 1:
```python
#Dado un nombre, responde cuantos caracteres tiene
name:str = input("Ingrese su nombre: ")
print(f"Su nombre tiene {len(name)} caracteres.")

```
### Ejercicio en clase 2:
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

### Ejercicio en clase 3: A
```python
#Dada una lista lis = [1, 2, 3, 4, 5]
#crear una nueva lista que por cada
#elemento x de lis, tenga x^2 en la lista nueva
lis: list[int] = [1, 2, 3, 4, 5]
lisC: list[int] = []
for i in lis:
    lisC.append(i*i)
print(lisC)
```
### Ejercicio en clase 3: B
```python
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

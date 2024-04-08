# Ejercicios con Chona

### Ejercicio 3: A
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
### Ejercicio 3: B
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

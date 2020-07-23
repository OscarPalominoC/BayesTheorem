# Bayes Theorem
Reto semana 9. Programa que calcula el Teorema de Bayes.

## Fórmula del Teorema de Bayes

Probabilidad de A y B
```
P(A and B) = P(A)* P(B|A)
```
Probabilidad de B
```
P(B) = P(A)* P(B|A) + P(¬A) * P(B|¬A)
```

**Terema de Bayes**
```
P(A | B) = (P(A) * P(B | A)) / P(B)
```

# Modo de uso

Todos los valores ingresados para que la salida sea correcta, deben ser ingresados en terminos de probabilidad, es decir, valores entre 0 - 1.

1. Se solicita el nombre de el conjunto a evaluar.
2. Se solicita el nombre de el conjunto contra la que se está evaluando.
3. Se solicita el nombre del evento a evaluar.
4. Se solicita la probabilidad que se elija el conjunto a evaluar.
5. Se solicita la probabilidad que se elija el conjunto a evaluar y el evento en concreto.
6. Se solicita la probabilidad que se elija el conjunto contra el que se esté evaluando y el evento en concreto.
7. Una vez ingresado estos datos, el programa devolverá un string descriptivo en el que se elije a un individuo del conjunto a evaluar y que cumpla la condición del evento. [Ejemplo](#ejemplo)


## Ejercicio 1.
Se hizo una encuesta a personas en las que se les preguntaba el género y si hacían ejercicios, los resultados fueron:

* 40% hombres
* 60% mujeres

El 80% de los hombres y el 50% de las mujeres dijeron que practicaban algún deporte o hacen ejercicios.

Conociendo estos datos, si se selecciona una persona al azar de las que respondió que hacía ejercicios ¿Cuál es la probabilidad que esta persona sea un hombre?

### Ejemplo
```
Cómo se llama el conjunto que deseas evaluar? hombres
Cómo se llama el conjunto contra la que estás evaluando? mujeres
Cómo se llama el evento que deseas evaluar? deporte
Cuál es la probabilidad que elijas el conjunto hombres? 0.4
Cuál es la probabilidad del evento deporte con el conjunto hombres? 0.8
Cuál es la probabilidad del evento deporte con el conjunto mujeres? 0.5
La probabilidad de elegir 1 hombres y que cumpla con deporte es 51.61 %
```

## Ejercicio 2.

En una fábrica de latas producen latas de dos tamaños, de 25 ml y de 40 ml, si se sabe que hacen la misma cantidad de ambas latas y que un 1% de las latas de 25ml y un 4% de las latas de 40ml salen defectuosas

¿Cuál es la probabilidad que al seleccionar una lata de las defectuosas al azar ésta sea de 40ml?

**Solución**

```
Cómo se llama el conjunto que deseas evaluar? Latas de 40 ml
Cómo se llama el conjunto contra la que estás evaluando? Latas de 25 ml
Cómo se llama el evento que deseas evaluar? Latas defectuosas
Cuál es la probabilidad que elijas el conjunto Latas de 40 ml? 0.5
Cuál es la probabilidad del evento Latas defectuosas con el conjunto Latas de 40 ml? 0.04
Cuál es la probabilidad del evento Latas defectuosas con el conjunto Latas de 25 ml? 0.01
La probabilidad de elegir 1 Latas de 40 ml y que cumpla con Latas defectuosas es 80.0 %
```

## Ejercicio 3.
En las elecciones de un país hay 2 candidatos a la presidencia, el candidato A y el candidato B y en los resultados de las selecciones se sabe que un 75% de el conjunto es de clase media y baja y un 25% son de son de clase alta, si por el candidato A votó un 90% de la clase alta y un 5% de la clase media y baja, y se elige una persona al azar de los que votaron por el candidato A.

¿Cuál es la probabilidad que este sea de la clase media y baja?

**Solución**

```
Cómo se llama el conjunto que deseas evaluar? Clase media y baja
Cómo se llama el conjunto contra la que estás evaluando? Clase alta
Cómo se llama el evento que deseas evaluar? Candidato A
Cuál es la probabilidad que elijas el conjunto Clase media y baja? 0.75
Cuál es la probabilidad del evento Candidato A con el conjunto Clase media y baja? 0.05
Cuál es la probabilidad del evento Candidato A con el conjunto Clase alta? 0.9
La probabilidad de elegir 1 Clase media y baja y que cumpla con Candidato A es 14.29 %
```
from bayes import Bayes

if __name__ == "__main__":
    loop = True
    while loop == True:
        population = input('Cómo se llama el conjunto que deseas evaluar? ')
        population2 = input('Cómo se llama el conjunto contra la que estás evaluando? ')
        event = input('Cómo se llama el evento que deseas evaluar? ')
        priorA = float(input(f'Cuál es la probabilidad que elijas el conjunto {population}? '))
        probBdadoA = float(input(f'Cuál es la probabilidad del evento {event} con el conjunto {population}? '))
        probBnoA = float(input(f'Cuál es la probabilidad del evento {event} con el conjunto {population2}? '))
        theorem = Bayes(priorA, probBdadoA, probBnoA)
        print(f'La probabilidad de elegir 1 {population} y que cumpla con {event} es {theorem.givenAandB()} %')
        choice = input('Deseas hacer otro calculo? S / N ')
        if choice == 's' or choice == 'S':
            loop = True
        else:
            loop = False
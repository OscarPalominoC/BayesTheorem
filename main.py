from bayes import Bayes

if __name__ == "__main__":
    loop = True
    while loop == True:
        population = input('Cómo se llama la población que deseas evaluar? ')
        event = input('Cómo se llama el evento que deseas evaluar? ')
        priorA = float(input(f'Cuál es la probabilidad que elijas a {population}? '))
        probBdadoA = float(input(f'Cuál es la probabilidad del evento {event}? '))
        theorem = Bayes(priorA, probBdadoA)
        print(f'La probabilidad de elegir 1 {population} y que cumpla con {event} es {theorem.givenAandB()} %')
        choice = input('Deseas hacer otro calculo? S / N ')
        if choice == 's' or choice == 'S':
            loop = True
        else:
            loop = False
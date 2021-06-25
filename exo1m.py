from random import choice


class Dé:
    def __init__(self):
        self.nombre_dé = [1,2,3,4,5,6]


class piece : 
    def __init__(self):
        self.List_piece_monnaie = ["Face","Pile"]


def Question1():
    
    nombre = choice(Dé().nombre_dé)

    print("Le chiffre est: ",nombre)


def Question2():
    
    n = int(input("Donner le nombre du lancement : "))
    apparence = []
    
    for i in range(n):
        apparence.append(choice(Dé().nombre_dé))
    print("Liste d'apparitions : ",apparence)


def apparence(objet):
    
    n = int(input("Donner le nombre du lancement : "))
    apparence = []
    
    for i in range(n):
        apparence.append(choice(objet))
    return apparence


def Question3():

    liste = apparence(Dé().nombre_dé)
    print("liste : ",liste)
    print("Nombre d'apparitions du 6  : ",liste.count(6))


def Question4():
    
    Question4_Liste = []
    
    while True :
        
        nombre = choice(Dé().nombre_dé)
        Question4_Liste.append(nombre)

        if nombre == 6 :
            break
    print("Liste d'apparitions : ",Question4_Liste)
    print("Nombre de lancements pour obtenir 6 : ",len(Question4_Liste))


def Question5():
    print(apparence(piece().List_piece_monnaie))

def switch_def ():
    
    while True : 
        print("\n\n***************Question 1 jusqu'à 5***************")

        choice = int(input("Choisir un type de Question : "))

        if choice == 1:
            Question1()

        elif choice == 2:
            Question2()
        
        elif choice == 3:
            Question3()

        elif choice == 4:
            Question4()

        elif choice == 5:
            Question5()
        
        elif choice == 6 : 
            break
        else : 
            print("Entree invalide")
            
      
      
if __name__ == '__main__':

    
    

    switch_def()
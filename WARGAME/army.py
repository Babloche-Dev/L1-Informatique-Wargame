import unity
import copy
import random

#--------Base de données---------#
ARMY_LIST_TABLE =["Armées des Humains","Armées des Gobelins","Armées des Elfes","Armées des Chevaliers de l'Integrité","Armées du Groupe 4","Armées des Pingouins","Armées des Peres Noel","Armées des Pinioufs","Armées de Pokémon","Shinobi de Konoha","Armée des Nains,","Alliance Rebelle,","Armée de l'Empire","Chevaliers Jedi","Alliance des Super Vilains"]

#-----------Classes--------#

class Army :

    def __init__(self,points):
        self.name=generate_name()
        self.unites=[]
        self.unites_copy =[]
        self.point=points
        self.nb_victory=0
        self.nb_match=0
        self.ratio=0
        self.probability=0

#--------générer-------#

    def generate_army(self):
        while self.point >= 3:
                unit= unity.Unit()
                if unit.point <= self.point:
                    self.point-=unit.point
                    self.unites.append(unit)



        self.unites_copy=copy.deepcopy(self.unites)




def generate_name():
    alea_name=random.choice(ARMY_LIST_TABLE)
    return alea_name

#-------------------------------------#

if __name__ == "__main__":
    a = Army(300)
    a.generate_army()
    print("Unites:", a.unites[1].name)
    print("Copy:", a.unites_copy[1].name)
    print(a.name)
    print(a.point)

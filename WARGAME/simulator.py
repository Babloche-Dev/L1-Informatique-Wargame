import unity
from random import randint
from random import choice
import army
import copy



#--------------Classe Simulateur-------------#

class Simulateur :

    def __init__(self,size):
        self.map=[]
        self.biomes=[] #inutilisé
        self.size=size


#----------------Générer------------------#

    def create_grid(self):
        self.map=[0]*self.size
        for i in range (self.size):
            self.map[i]=[0]*self.size
            for y in range (self.size):
                self.map[i][y]=[0]*2

    def affiche (self):
        for x in self.map:
            for y in x:
                s = 0 if y[1] == 0 else y[1].name
                print (s," ",end="")
            print ()



#----------------trouver une unité---------------------#


    def find_unity(self,grid,unit):
        for i in range(self.size):
            for j in range(self.size):
                if grid[i][j][1]==unit:
                    return(i,j)




#----------------Placer une unité---------------------#

    def set_unity(self,unit):
        self.map[unit.x][unit.y][1] = unit


    def set_army1(self,army):
        c=0
        d=0
        for unit in army.unites:
            if c > self.size-1:
                d+=1
                c=0
            else :
                unit.x+=c
                unit.y+=d
                self.set_unity(unit)
                c+=1

    def set_army2(self,army):
        c=0
        d=self.size-1
        for unit in army.unites:
            if c > self.size-1 :
                d-=1
                c=0
            else :
                unit.x+=c
                unit.y+=d
                self.set_unity(unit)
                c+=1


#----------Notion de Combat/Mort----------#

    def death_unity(self,army1,army2):
        for liste in self.map:
            for s_liste in liste:
                if s_liste[1]==0:
                	None
                else :
                    if s_liste[1].hp<=0 :
                        if s_liste[1] in army1.unites :
                            army1.unites.remove(s_liste[1])
                            self.map[s_liste[1].x][s_liste[1].y][1]=0
                        else :
                            army2.unites.remove(s_liste[1])
                            self.map[s_liste[1].x][s_liste[1].y][1]=0



    def target(self,unit,army_enemy):
        for unit2 in army_enemy.unites :
            x= unit.x - unit2.x
            y= unit.y - unit2.y 
            if(x,y) in [(0,1),(1,0),(0,-1),(-1,0)]:
                unit.hit(unit2)


#----------------se deplacer---------------------#

    def can_deplace(self,army,army2):
        select_unity=choice(army.unites)
        save_x=select_unity.x
        save_y=select_unity.y
        self.deplace(select_unity,army,army2)

        if select_unity.x < 0:
            select_unity.x = 0
        if select_unity.x > self.size - 1:
            select_unity.x = self.size - 1
        if select_unity.y < 0:
            select_unity.y = 0
        if select_unity.y > self.size - 1:
            select_unity.y = self.size -1
        if self.map[select_unity.x][select_unity.y][1]!=0:
            select_unity.x=save_x
            select_unity.y=save_y
            print("-----------------------------")
            print(select_unity.name,"n'a pas bougé")
        else :
            self.set_unity(select_unity)
            self.map[save_x][save_y][1] = 0
            print("-----------------------------")
            print(select_unity.name,"vient de se déplacer")

        print("--------------------")
        for a in army.unites:
            print(a.name, end=', ')
        print()
        self.affiche()
        return select_unity

    def deplace(self,unit,army,army2):
        rand=randint(1,4)
        if rand==1:
            self.front(unit,army,army2)
        elif rand==2:
            self.right(unit,army,army2)
        elif rand==3 :
            self.left(unit,army,army2)
        else :
            self.back(unit,army,army2)

#------notion de déplacement ---------#

    def front(self,unit,army,army2):
        if unit in army.unites :
            unit.x+=1
            unit.y+=0
        elif unit in army2.unites :
            unit.x+=0
            unit.y-=1


    def right(self,unit,army,army2):
        if unit in army.unites :
            unit.x+=0
            unit.y-=1
        elif unit in army2.unites  :
            unit.x+=0
            unit.y+=1

    def left(self,unit,army,army2):
        if unit in army.unites:
            unit.x+=0
            unit.y+=1
        elif unit in army2.unites :
            unit.x+=0
            unit.y-=1

    def back(self,unit,army,army2):
        if unit in army.unites:
            unit.x-=1
            unit.y+=0
        elif unit in army2.unites :
            unit.x+=1
            unit.y+=0

#----------Notion de Jeu/Tour-----------------------#

    def jeu (self,army_attaque,army_defense):
        i=0
        while(self.win_army(army_attaque,army_defense)==None):
            self.tour(army_attaque,army_defense)
            self.tour(army_defense,army_attaque)
            self.death_unity(army_attaque,army_defense)
            i+=2
            
        print("Tour actuel : ",i)
        print("l'armée qui a gagné est : ",self.win_army(army_attaque,army_defense))
        army_defense.unites = army_defense.unites_copy                  #à regrouper dans une fonction ?
        army_defense.unites_copy = copy.deepcopy( army_defense.unites)
        army_attaque.unites = army_attaque.unites_copy
        army_attaque.unites_copy = copy.deepcopy( army_attaque.unites)


    def tour(self,army_attaque,army_defense):
        self.can_deplace(army_attaque,army_defense)
        self.target(self.can_deplace(army_attaque,army_defense),army_defense)



#----------Notion de Victoire/Defaite----------#

    def win_army(self,army1,army2):
        if army1.unites and army2.unites:
            return None
        else :
            if not army1.unites:
                army2.nb_victory+=1
                army2.nb_match+=1
                army1.nb_match+=1
                return army2

            else:
                army1.nb_victory+=1
                army1.nb_match+=1
                army2.nb_match+=1
                return army1

def game(army1,army2):
    simulation=Simulateur(16)
    grid = simulation.create_grid()
    simulation.set_army1(army1)
    simulation.set_army2(army2)
    simulation.jeu(army1,army2)
    print(army1)
    print(army2)

#---------------------------------------------------#
if __name__ == "__main__":
    J1=army.Army(300)
    J1.generate_army()
    J2=army.Army(300)
    J2.generate_army()
    game(J1,J2)

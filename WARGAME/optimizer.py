import unity
from random import *
import army
import simulator


#-------------Class Optimisateur----------------------#

class Optimizer :
        def __init__(self):
                self.armies =[]
                self.total_ratio = 0
                self.total_probability = 0
                self.news_armies_generation = []



#---------Générer liste d'armées----------------------#

        def armies_liste(self,n,points):
                i=0
                while(i<n):
                        army1=army.Army(points)
                        army1.generate_army()
                        self.armies.append(army1)
                        i+=1

        def tournament(self,n):
            for first in self.armies:
                for second in self.armies:
                    if first != second:
                        i = 0
                        while i < n:
                            simulator.game(first,second)
                            i+=1
        

        def ratio(self):
            for armee in self.armies:
                armee.ratio = armee.nb_victory / armee.nb_match if armee.nb_match > 0 else 0
                self.total_ratio+= armee.ratio



        def roulette_whell_selection(self,k):
            for arm in self.armies:
                arm.probability = arm.ratio / self.total_ratio if self.total_ratio > 0 else 0
                self.total_probability += arm.probability
            for element in range(0,k):
                nb_random = random()
                relation = nb_random * self.total_probability
                for arms in self.armies:
                    if arms.probability < relation:
                        relation+= arms.probability
                    else :
                        self.news_armies_generation.append(arms)
                        break

        def crossing_over(self):
            while len(self.news_armies_generation) < len(self.armies):
                i = randint(0,len(self.armies)-1)
                j = randint(0,len(self.armies)-1)
                new_army = army.Army(300)
                new_army2 = army.Army(300)
                for value, troup in enumerate(self.armies[i].unites,0):
                    for value_2, troup2 in enumerate(self.armies[j].unites,0):
                        nbr_random = randint(0,1)
                        if nbr_random == 0:
                            new_army.unites.append(self.armies[i].unites[value])
                            new_army.point -= self.armies[i].unites[value].point
                            new_army2.unites.append(self.armies[j].unites[value_2])
                            new_army2.point -= self.armies[j].unites[value_2].point
                        else:
                            new_army.unites.append(self.armies[j].unites[value_2])
                            new_army.point -= self.armies[j].unites[value_2].point
                            new_army2.unites.append(self.armies[i].unites[value])
                            new_army2.point -= self.armies[i].unites[value].point
                if new_army.point >= 0 :
                    news_armies_generation.append(new_army)
                else: 
                    while new_army.point < 0:
                        r = randint(0,len(new_army.unites)-1)
                        new_army.point += new_army.unites[r].point
                        new_army.unites.remove(new_army.unites[r])
        

                if len(self.news_armies_generation) < len(self.armies):
                    if new_army2.point >= 0:
                        self.news_armies_generation.append(new_army2)
                    else: 
                        while new_army2.point < 0:
                            r = randint(0,len(new_army2.unites)-1)
                            new_army2.point += new_army2.unites[r].point
                            new_army2.unites.remove(new_army2.unites[r])
        
                        self.news_armies_generation.append(new_army2)


        #def mutation(self):



#-----------------------------------------------------#
if __name__ =="__main__":
        p=Optimizer()
        p.armies_liste(5,300)
        p.tournament(10)
        p.ratio()
        p.roulette_whell_selection(2)
        p.crossing_over()
        print(len(p.armies))
        print(len(p.news_armies_generation))
        

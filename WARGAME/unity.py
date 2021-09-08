#----Base de données---#
import random
from random import randint

NAME_LIST_TABLE =["Valentin","Brandon","Edgar","Thomas","Pingouin","Alice","Arthur","Alienor","Astrid","Louis","Accolon","Agravain","Bedivere","Bohort",
"Caradoc","Gaheris,","Gahalad","Gareth","Hector","Keu","Hunbaut","Lancelot","Lionel","Mordred","Mannfred","Perceval","Tristan","Yvain","Grenuit","Oulbare"
,"Crounch"] 
XP_TABLE = {1:0,2:500,3:1200,4:2000,5:3000}
HP_TABLE={1:100,2:150,3:200,4:250,5:350}
AP_TABLE={"Tissu":30,"Cuir":45,"Fer":60}

UNITY_GARNISON={}
ENEMY_GARNISON={}

#----Déclaration des classes ------#

class Unit :

    def __init__(self):
        self.name=generate_name()
        self.level=generate_level()
        self.weapon=generate_weapon()
        self.xp=generate_xp(self.level,self)                       
        self.hp=generate_hp(self.level)
        self.armor=generate_armor(self.weapon)
        self.point = generate_point(self.weapon,self.level)
        self.movement = generate_movement(self.armor) #pour l'instant inutilisé
        self.x=0
        self.y=0



    def get_level(self):
        result=0
        for level,xp in XP_TABLE.items():
            if self.xp>=xp:
                result=level
                self.get_hp(result)
            else :
                break
        return result

    def get_hp(self,level):                           
        result=0
        for level_hp,hp in HP_TABLE.items():
            if level_hp == level :
                result = hp

        return result

    def hit(self,cible):
        if self.weapon.name == "Sceptre":
            cible.hp+=self.weapon.damage
            if cible.hp > HP_TABLE[cible.level]:
                cible.hp = HP_TABLE[cible.level]
            #print(cible.name,"a ete soigné de",self.weapon.damage,"hp par",self.name,"\n Armure restante :",cible.armor.ap,"AP","\n Vie restante :",cible.hp,"HP")


        else:
            if cible.armor.ap>0:
                cible.armor.ap-=self.weapon.damage
                if cible.armor.ap<0:
                    cible.hp+=cible.armor.ap
                    cible.armor.ap=0
                #print(cible.name,"a pris",self.weapon.damage,"de degats par",self.name,"\n Armure restante :",cible.armor.ap,"AP","\n Vie restante :",cible.hp,"HP")
            elif cible.armor.ap<=0:
                cible.hp-=self.weapon.damage
                #print(cible.name,"a pris",self.weapon.damage,"de degats par",self.name,"\n Armure restante :",cible.armor.ap,"AP","\n Vie restante :",cible.hp,"HP")      






#-----Générer------#
def generate_name():
    alea_name=random.choice(NAME_LIST_TABLE)

    return alea_name

def generate_level():
    return randint(1,5)

def generate_armor(weapon):
    if weapon.name=='Dague' or weapon.name=='Arc':
        return Cuir()
    elif weapon.name=='Eppée' or weapon.name=='Lance':
        return Fer()
    else :
        return Tissu()

def generate_weapon():
    number=randint(1,6)
    if number==1:
        return Dague()
    elif number==2:
        return Eppée()
    elif number==3:
        return Lance()
    elif number==4:
        return Arc()
    elif number==5:
        return Baton()
    else :
        return Sceptre()

def generate_xp(level,self):
    if level == 1:
        return 0
    elif level ==2:
        return 500
    elif level ==3:
        return 1200
    elif level == 4:
        return 2000
    else :
        return 3000

def generate_hp(level):
    if level==1:
        return 100
    elif level==2:
        return 150
    elif level==3:
        return 200
    elif level==4:
        return 250
    else :
        return 350

def generate_point(weapon,level):
    point = level + weapon.point
    return point


def generate_movement(armor): #inutilisé 
    if armor == Fer() :
        return 1
    elif armor == Cuir():
        return 2
    else :
        return 3

#----Classe Armes-------#
class Arme :                                             

    def __init__(self,name,damage,point):
        self.name=""
        self.damage=""
        self.point=""               

class Dague(Arme):

    def __init__(self):
        self.name="Dague"
        self.damage=25
        self.point=2

class Eppée (Arme):

    def __init__(self):
        self.name="Eppée"
        self.damage=35
        self.point=4

class Lance(Arme):

    def __init__(self):
        self.name="Lance"
        self.damage=55
        self.point=6

class Arc(Arme):

    def __init__(self):
        self.name="Arc"
        self.damage=45
        self.point=5

class Baton(Arme):

    def __init__(self):
        self.name="Baton"
        self.damage=20            
        self.point=4

class Sceptre(Arme):                
    def __init__(self):
        self.name="Sceptre"
        self.damage=30
        self.point=4

#--Classe Point D'armure---#
class Armure :

    def __init__(self):
        self.name=""
        self.ap=""

class Tissu (Armure) :

    def __init__(self):
        self.name="Tissu"
        self.ap=30

class Cuir (Armure):

    def __init__(self):
        self.name="Cuir"
        self.ap=45

class Fer(Armure):

    def __init__(self):
        self.name="Fer"
        self.ap=60



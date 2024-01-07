class Army:
    def __init__(self):
        self.soldiers = []
        self.size = 0
    
    def add_units(self, class_unit, amount):
        for _ in range(amount):
            self.soldiers.insert(0,class_unit())
        self.size += amount


class Warrior:
    def __init__(self, health=50, attack=5, defense = 0, vampirism = 0):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self, health=50):
        super().__init__(health, 7)

class Defender(Warrior):
    def __init__(self):
        super().__init__(60,3,2)

class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1

class Vampire(Warrior):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Battle:
    def fight(self, army1, army2):
        while army1.size > 0 and army2.size > 0:
            attack1 = army1.soldiers[0].attack
            attack2 = army2.soldiers[0].attack
            defense1 = army1.soldiers[0].defense
            defense2 = army2.soldiers[0].defense
            vampirism1 = (army1.soldiers[0].vampirism)/100
            vampirism2 = (army2.soldiers[0].vampirism)/100   
            if attack1>=defense2:
                army2.soldiers[0].health -= (attack1-defense2)
                army1.soldiers[0].health += (attack1-defense2)*vampirism1
            if attack2>=defense1 and army2.soldiers[0].is_alive == True:
                army1.soldiers[0].health -= (attack2-defense1)
                army2.soldiers[0].health += (attack2-defense1)*vampirism2

            if not army1.soldiers[0].is_alive:
                army1.soldiers.pop(0)
                army1.size -= 1

            elif not army2.soldiers[0].is_alive:
                army2.soldiers.pop(0)
                army2.size -= 1
        print(army1.size)
        print(army2.size)
        return army1.size > 0
def flght(w1,w2):
    attack1 = w1.attack
    attack2=w2.attack
    defense1 = w1.defense
    defense2 = w2.defense
    vampirism1 = (w1.vampirism)/100
    vampirism2 = (w2.vampirism)/100
    
    while w1.is_alive ==True and w2.is_alive==True:
        if attack1>=defense2:
            w2.health -= (attack1-defense2)
            health2 = w2.health
            w1.health += (attack1-defense2)*vampirism1
            health1 = w1.health
        if attack2>=defense1 and w2.is_alive == True:
            w1.health -= (attack2-defense1)
            health1 = w1.health
            w2.health += (attack2-defense1)*vampirism2
            health2 = w2.health
        if w1.is_alive == False:
            return False
        elif w2.is_alive == False:
            return True

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
print(flght(bob, mike))


my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

battle = Battle()

print(battle.fight(my_army, enemy_army))
print(battle.fight(army_3, army_4))



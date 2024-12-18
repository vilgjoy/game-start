class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

        # private attribute - something that shouldn't be changed
        self._id = 5
    def attack(self,amount):
        print('The monster attacked!')
        print(f'{amount} damage was dealt!')
        self.energy -= 20
    
    def move(self,speed):
        print('The monster moved')
        print(f'It has a speed of {speed}')


monster = Monster(20,10)
if (hasattr(monster,'health')):
    print(f'the monster has {monster.health} health')
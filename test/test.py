class Doggy:
    birth_of_dogs = 0
    num_of_dogs = 0
    def __init__(self, name, type):
        self.name = name
        self.type = type
        Doggy.num_of_dogs += 1

    def bark(self):
        print('bow!')
    
    @classmethod
    def birth_dog(cls):
        cls.num_of_dogs += 1
        cls.birth_of_dogs += 1
    
    @classmethod
    def death_dog(cls):
        cls.num_of_dogs -= 1
    
    def get_status():
        print(f'태어난 개 : {Doggy.birth_of_dogs}마리/n총 개 : {Doggy.num_of_dogs}마리')

sangeun = Doggy('상근이', '삽살개')
print(Doggy.get_status())
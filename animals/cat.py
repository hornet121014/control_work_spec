from animals.pets import Pets

class Cat(Pets):
    def __init__(self, animals_name, pets_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pets_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth


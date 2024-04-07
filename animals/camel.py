from animals.pack_animals import PackAnimals

class Camel(PackAnimals):
    def __init__(self, animals_name, pack_animals_name, animal_name, animal_command, animal_birth):
        super().__init__(animals_name, pack_animals_name)
        self.animal_name = animal_name
        self.animal_command = animal_command
        self.animal_birth = animal_birth
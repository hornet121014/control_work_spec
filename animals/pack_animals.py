from animals.animals import Animals

class PackAnimals(Animals):
    def __init__(self, animals_name, pack_animals_name):
        super().__init__(animals_name)
        self.pack_animals_name = pack_animals_name

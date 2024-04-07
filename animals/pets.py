from animals.animals import Animals

class Pets(Animals):
    def __init__(self, animals_name, pets_name):
        super().__init__(animals_name)
        self.pets_name = pets_name

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes sound")

    def eat(self):
        print(f"{self.name} is eating.")

    def get_info(self):
        return f'{self.__class__.__name__},{self.name},{self.age}'

class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} makes sound (Bird)")

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying!")
        else:
            print(f"{self.name} cannot fly.")

    def get_info(self):
        return f'Bird,{self.name},{self.age},{self.can_fly}'

class Mammal(Animal):
    def __init__(self, name, age, is_domestic):
        super().__init__(name, age)
        self.is_domestic = is_domestic

    def make_sound(self):
        print(f"{self.name} makes sound (Mammal)")

    def get_info(self):
        return f'Mammal,{self.name},{self.age},{self.is_domestic}'

class Reptile(Animal):
    def __init__(self, name, age, is_venomous):
        super().__init__(name, age)
        self.is_venomous = is_venomous

    def make_sound(self):
        print(f"{self.name} makes sound (Raptile)!")

    def get_info(self):
        return f'Reptile,{self.name},{self.age},{self.is_venomous}'

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the zoo.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} has been added as staff.")

    def list_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(f'- {animal.name}, Age: {animal.age}')

    def list_staff(self):
        print("Staff in the zoo:")
        for staff in self.staff:
            print(f'- {staff.name}, Role: {staff.__class__.__name__}')

    def save_to_file(self, Zoo_data):
        with open(Zoo_data, 'w') as f:
            f.write("Animals\n")
            for animal in self.animals:
                f.write(animal.get_info() + '\n')
            f.write("Staff\n")
            for staff in self.staff:
                f.write(f'{staff.__class__.__name__},{staff.name}\n')
        print(f"Zoo data saved to {Zoo_data}.")

    def load_from_file(self, Zoo_data):
        try:
            with open(Zoo_data, 'r') as f:
                lines = f.readlines()
                mode = None
                for line in lines:
                    line = line.strip()
                    if line == "Animals":
                        mode = "Animals"
                        continue
                    elif line == "Staff":
                        mode = "Staff"
                        continue

                    # Загрузка животных
                    if mode == "Animals":
                        parts = line.split(',')
                        animal_type = parts[0]
                        name = parts[1]
                        age = int(parts[2])

                        if animal_type == "Bird":
                            can_fly = parts[3] == "True"
                            animal = Bird(name, age, can_fly)
                        elif animal_type == "Mammal":
                            is_domestic = parts[3] == "True"
                            animal = Mammal(name, age, is_domestic)
                        elif animal_type == "Reptile":
                            is_venomous = parts[3] == "True"
                            animal = Reptile(name, age, is_venomous)
                        else:
                            animal = Animal(name, age)

                        self.add_animal(animal)

                    # Загрузка сотрудников
                    elif mode == "Staff":
                        parts = line.split(',')
                        staff_type = parts[0]
                        name = parts[1]

                        if staff_type == "ZooKeeper":
                            staff_member = ZooKeeper(name)
                        elif staff_type == "Veterinarian":
                            staff_member = Veterinarian(name)
                        else:
                            staff_member = Staff(name)

                        self.add_staff(staff_member)

            print(f"Zoo data loaded from {Zoo_data}.")
        except FileNotFoundError:
            print(f"{Zoo_data} not found. Starting with an empty zoo.")

class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f'{self.name} is feeding {animal.name}.')

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f'{self.name} is healing {animal.name}.')



zoo = Zoo()

zoo.load_from_file('zoo_data.txt')

parrot = Bird(name="Parrot", age=3, can_fly=False)
lion = Mammal(name="Lion", age=5, is_domestic=False)
snake = Reptile(name="Snake", age=2, is_venomous=True)

zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)

keeper = ZooKeeper(name='Keeper')
vet = Veterinarian(name='Veterinarian')

zoo.add_staff(keeper)
zoo.add_staff(vet)

zoo.save_to_file('zoo_data.txt')

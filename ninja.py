class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy+= 25
        print("Increased pets energy by 25")
        return self
    
    def eat(self):
        self.energy+= 5
        self.health+=10
        print("Increased energy by 5, and health by 10")
        return self
    
    def play(self):
        self.health+= 5
        print("pets energy increased by 5")
        return self

    def noise(self):
        print("Woof Woof, Bark Bark, or something")
        return self


class Ninja(Pet):
    def __init__(self, first_name, last_name, pet, treats, pet_food, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


    def walk(self):
        self.play()
        return self
    
    def feed(self):
        self.eat()
        return self
    
    def bathe(self):
        self.noise()
        print("Your pet is clean :)")
        return self

    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\n Pet Type: {self.pet}\n Favorite Treat: {self.treats}\n Food: {self.pet_food}")
        print(f"Pet name: {self.name}\n Pet Type: {self.type}\n Tricks: {self.tricks}\n Current Health: {self.health}\n Current energy: {self.energy}")
        return self
    
    def display_pet_stats(self):
        print("*"*80)
        print(f"Current Health: {self.health}\n Current energy: {self.energy}")
        return self

user1 = Ninja("Josh", "Pumpkins", "Dog", "BaconStrips", "kibble", "Pookie", "Labrador", "Sit, Stay, Bark", 100, 50)
user1.display_info().walk().feed().bathe().display_pet_stats()
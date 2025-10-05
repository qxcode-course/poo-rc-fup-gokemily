class Animal: 
    def __init__(self, species: str = "", sound: str = ""):
        self.species = species
        self.sound = sound
        self.age = 0

    def ageBy(self, increment: int) -> None:
        if self.age + increment == 4:
            print(f"warning: {self.species} morreu")
            self.age += increment
        elif self.age + increment > 4:
            print(f"warning: {self.species} morreu")
        else:
            self.age += increment

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        else:
            return self.sound

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

def main():
    animal = Animal()
    while True:
        line: str = input()

        arg: list[str] = line.split(" ")

        print("$" + line)
        if arg[0] == "end":
            break
        elif arg[0] == "grow":
            animal.ageBy(int(arg[1]))
        elif arg[0] == "noise":
            print(animal.makeSound())
        elif arg[0] == "init":
            animal : Animal = Animal(arg[1],arg[2])
        elif arg[0] == "show":
            print(animal)
        else:
           print("Comando nao encontrado")

main()
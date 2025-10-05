class Animal: 
    def _init_(self, species: str = "", sound: str = ""):
        self.species = species
        self.sound = sound
        self.age = 0


    def _str_(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"
def main():
    animal = Animal()
    while True:
        line: str = input()
        arg: list[str] = line.split(" ")
        print("$" + line)
        if arg[0] == "end":
            break
        elif arg[0] == "init":
            animal : Animal = Animal(arg[1],arg[2])
        elif arg[0] == "show":
            print(animal)
        else:
           print("Comando nao encontrado")

main()
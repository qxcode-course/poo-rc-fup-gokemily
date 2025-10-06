class Car:
    def __init__(self):
        self.passengers: int = 0
        self.km: int = 0
        self.passMax: int = 2
        self.gas: int = 0
        self.gasMax: int = 100
    
    def __str__(self) -> str:
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"
    
    def enter(self) -> None:
        if self.passengers == self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.passengers += 1
    
    def sair(self) -> None:
        if self.passengers == 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passengers -= 1
    
    def fuel(self, increment: int) -> int:
        if self.gas + increment > self.gasMax:
            self.gas = self.gasMax
        else:
            self.gas += increment
    
    def drive(self, increment: int) -> int:
        if self.passengers == 0:
            print("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print("fail: tanque vazio")
        elif self.gas - increment < 0:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        else:
            self.km += increment
            self.gas -= increment

def main():
    carro = Car()
    while True:
        line: str = input()

        arg: list[str] = line.split(" ")

        print("$" + line)
        if arg[0] == "end":
            break
        elif arg[0] == "enter":
            carro.enter()
        elif arg[0] == "leave":
            carro.sair()
        elif arg[0] == "fuel":
            carro.fuel(int(arg[1]))
        elif arg[0] == "show":
            print(carro)
        elif arg[0] == "drive":
            carro.drive(int(arg[1]))
        else:
           print("Comando nao encontrado")

main()
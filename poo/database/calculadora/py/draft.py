class Calculadora:
    def __init__(self, baterryMax: int):
        self.battery = 0
        self.batteryMax = baterryMax
        self.display = 0
    
    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def recarregar(self, increment: int) -> None:
        if self.battery + increment <= self.batteryMax:
            self.battery += increment
        else:
            self.battery = self.batteryMax
    
    def somar(self, a: int, b: int) -> int:
        if self.battery == 0:
            print("fail: bateria insuficiente")
        else:
            self.display = a + b
            self.battery -= 1
    
    def divisao(self, a: int, b: int) -> int:
        if self.battery == 0:
            print("fail: bateria insuficiente")
        elif b == 0:
            print("fail: divisao por zero")
            self.battery -= 1
        else:
            self.display = a / b
            self.battery -= 1
    
def main():
    calculadora = Calculadora(5)
    while True:
        line: str = input()

        arg: list[str] = line.split(" ")

        print("$" + line)
        if arg[0] == "end":
            break
        elif arg[0] == "sum":
            calculadora.somar(int(arg[1]), int(arg[2]))
        elif arg[0] == "charge":
            calculadora.recarregar(int(arg[1]))
        elif arg[0] == "div":
            calculadora.divisao(int(arg[1]), int(arg[2]))
        elif arg[0] == "init":
            calculadora = Calculadora(int(arg[1]))
        elif arg[0] == "show":
            print(calculadora)
        else:
           print("Comando nao encontrado")

main()
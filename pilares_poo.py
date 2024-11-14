
# exemplo de herança
print("\nExemplo de herança:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

# Polimorfismo permite que objetos de diferentes classes sejam tratados como objetos de uma classe comum

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

print("\nExemplo de polimorfismo")
animais = [dog, cat]


for animal in animais:
    print (f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsolamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor = 500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor =- 500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor = 200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veculo(ABC):

    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veculo):
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro deslgado usando a chave"
    
carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())















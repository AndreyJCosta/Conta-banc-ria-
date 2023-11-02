class Banco:
    def __init__(self, numero, saldo, nome, tipo, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.limite = limite
        self.status = False
        self.saldoDevedor = 0

    def ativarConta(self):
        if self.status == False:
            print (f"A conta já está ativa em nome de {self.nome}.")
            self.status = True
        else:
            print (f"Já existe uma conta no nome de {self.nome}!")

    def depositar(self, valor):
        if self.status == False:
            print(f'{self.nome} não possui conta ativa.')
        else:
            if valor > 0:
                if self.saldoDevedor > 0:
                    if self.saldoDevedor >= valor:
                        self.saldoDevedor -= valor
                        print(f"Você reduziu sua dívida em {valor:.2f}. Seu novo saldo devedor é {self.saldoDevedor: 2f}.")
                    else:
                        valor -= self.saldoDevedor
                        self.saldoDevedor = 0
                        self.saldo += valor
                        print(f"Saldo anterior = {self.saldo - valor:.2f} \n")
                        print(f"Novo saldo é {self.saldo:.2f}.")
                else:
                    print(f"Saldo anterior = {self.saldo:.2f}. \n")
                    self.saldo += valor
                    print(f"Novo saldo = {self.saldo:.2f}.")
            else:
                print("Valor de depósito inválido")

    def sacar(self, valor):
        if self.status == False:
            print(f"{self.nome} não possui conta ativa")
        else:
            if self.saldo > valor:
                if (self.saldo + self.limite - self.saldoDevedor) >= valor:
                    self.saldoDevedor += valor - self.saldo
                    self.saldo = 0
                    return (f" O saldo devedor é {self.saldoDevedor:.2f}")
                else:
                    return ("Saldo insuficiente.")
            else:
                return (f"Saldo anterior = {self.saldo:.2f}!")
                self.saldo -= valor
                print(f"Novo Saldo é {self.saldo:.2f}")

    def verificarSaldo(self):
        if self.saldo == False:
            return (f" {self.nome} ainda não possui nenhuma conta ativa!")
        else:
            if self.saldo >= 0:
                return (f"O saldo da conta é de {self.saldo:.2f}.")

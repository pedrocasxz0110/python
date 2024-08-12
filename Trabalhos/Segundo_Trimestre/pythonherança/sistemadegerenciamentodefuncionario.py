class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f'Nome: {self.nome}, Salário Base: R${self.salario_base:.2f}, Salário: R${self.calcular_salario():.2f}'


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus

    def __str__(self):
        return f'{super().__str__()}, Bônus: R${self.bonus:.2f}'


class Operario(Funcionario):
    def __init__(self, nome, salario_base, horas_extras):
        super().__init__(nome, salario_base)
        self.horas_extras = horas_extras
        self.valor_hora_extra = 20

    def calcular_salario(self):
        return self.salario_base + (self.horas_extras * self.valor_hora_extra)

    def __str__(self):
        return f'{super().__str__()}, Horas Extras: {self.horas_extras}, Valor Horas Extras: R${(self.horas_extras * self.valor_hora_extra):.2f}'


class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def mostrar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)




empresa = Empresa()

gerente = Gerente("Ana", 5000, 1500)
operario = Operario("Carlos", 2000, 10)

empresa.adicionar_funcionario(gerente)
empresa.adicionar_funcionario(operario)

print("Funcionários da empresa:")
empresa.mostrar_funcionarios()

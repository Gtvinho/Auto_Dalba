class Veiculo:
    def __init__(self, prefixo, quantidade, horimetro, hodometro, horario, posto, data):
        self.data = data
        self.prefixo = prefixo
        self.quantidade = quantidade
        self.horimetro = horimetro
        self.hodometro = hodometro
        self.horario = horario
        self.posto = posto
    def __str__(self):
        return (f"Prefixo: {self.prefixo}, Quantidade: {self.quantidade}, "
                f"Horímetro: {self.horimetro}, Hodômetro: {self.hodometro}, "
                f"Horário: {self.horario.strftime('%H:%M')}")

class Entity:
    def __init__(self):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.ativo = ativo
        self.especialidade = especialidade
    def situacao(self):
        return "Ativo" if self.ativo else "Não ativo"

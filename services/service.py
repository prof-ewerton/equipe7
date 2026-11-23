from repository.dao_entity import DAOEntity

class Services:

    def __init__(self, dinossauros):
        self.dinossauros = pesquisadores

    def criar_dinossauro(self, nome, idade, carnivoro, especie):
        if nome is None or nome.strip() == "":
            raise ValueError("Você deve preencher o nome")
        dinossauro = (nome.strip(), (especialidade or "").strip(), 0)
        return self.dinossauros.create(dinossauros)

    def listar_dinossauros(self):
        return self.dinossauros.find_all()

    def pegar_dinossauros(self, dinossauros_id):
        return self.dinossauros.find_by_id(dinossauros_id)

    def atualizar_pesquisador(self, nome, idade, carnivoro, especie):
        if nome is None or nome.strip() == "":
            raise ValueError("Você deve preencher o nome")
        atual = self.dinossauros.find_by_id(dinossauros_id)
        if atual is None:
            return False
        dinossauro = (nome.strip(), (especie or "").strip(), atual[3], dinossauro_id)
        return self.dinossauros.update(dinossauro)

    def pegar_dinossauro(self, dinossauro_id):
        if self.dinossauros.find_by_id(dinossauro_id) is None:
            return False
        return self.dinossauros.delete(dinossauro_id)





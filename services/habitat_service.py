class Habitat_Service:
    def __init__(self, habitat):
        self.habitat = habitat
    
    def criar_habitat(self, nome, capacidade, seguro, bioma):
        if nome is None or nome.strip() == "":
            raise ValueError("Você deve preencher o nome")
        habitat = (nome.strip(), (bioma or "").strip(), 0)
        return self.create(habitat)

    def listar_habitat(self):
        return self.habitats.find_all()

    def pegar_habitat(self, habitat_id):
        return self.habitats.find_by_id(habitat_id)

    def atualizar_habitat(self, nome, capacidade, seguro, bioma):
        if nome is None or nome.strip() == "":
            raise ValueError("Você deve preencher o nome")
        atual = self.habitats.find_by_id(habitat_id)
        if atual is None:
            return False
        habitat = (nome.strip(), (bioma or "").strip(), atual[3], habitat_id)
        return self.habitats.update(habitat)
    
from repository.dao_entity import DAOEntity

class Services:

    def __init__(self, pesquisadores):
        self.pesquisadores = pesquisadores

    def criar_pesquisador(self, nome, idade, ativo, especialidade):
        if nome is None or nome.strip() == "":
            raise ValueError("Você deve preencher o nome")
        pesquisador = (nome.strip(), (especialidade or "").strip(), 0)
        return self.pesquisadores.create(pesquisador)

    def listar_pesquisador(self):
        return self.pesquisadores.find_all()

    def pegar_pesquisador(self, pesquisador_id):
        return self.pesquisadores.find_by_id(pesquisador_id)

    def atualizar_pesquisador(self, nome, idade, ativo, especialidade):
        if nome is None or nome.strip() == "":
            raise ValueError("Você deve preencher o nome")
        atual = self.pesquisadores.find_by_id(pesquisador_id)
        if atual is None:
            return False
        pesquisador = (nome.strip(), (especialidade or "").strip(), atual[3], pesquisador_id)
        return self.pesquisadores.update(pesquisador)

    def pegar_pesquisador(self, pesquisador_id):
        if self.pesquisadores.find_by_id(pesquisador_id) is None:
            return False
        return self.pesquisadores.delete(pesquisador_id)


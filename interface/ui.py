class Ui:

    def __init__(self):
        self.MENU_OPTIONS = [
            (1, "Entity one", self.menu_entity_one),
            (3, "Pesquisador", self.menu_entity_three),
        ]

    def show(self):
        while True:
            print("\n===== Parque Jurássico - Mundo dos dinossauros =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")              

            if option == "0":
                print("Encerrando...")
                break
            
            elif option == "3":
                nome = str(input("Nome: "))
                idade = int(input("Idade: "))
                ativo = bool(input("Ativo? "))
                especialidade = str(input("Especialidade: "))
                try:
                    novo_id = self.services.criar_pesquisador(nome, especialidade)
                    print(f"Pesquisador cadastrado com sucesso! ID: {novo_id}")
                except ValueError as erro:
                    print(f"Erro: {erro}")
            
            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== TEMA DA EQUIPE =====")
        print("= Entidade do Estudante ==")
    
    def menu_entity_three(self):
        print("\n===== Parque Jurássico - Mundo dos dinossauros =====")
        print("= Pesquisador ==")
        
        
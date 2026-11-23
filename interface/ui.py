class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Entity one", self.menu_entity_one),
        ]

    def show(self):
        while True:
            print("\n===== TEMA DA EQUIPE =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break

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

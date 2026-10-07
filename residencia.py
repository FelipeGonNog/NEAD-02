class Comodo:
    def __init__(self, nome, area):
        self.nome = nome
        self.area = area


class Residencia:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)
        self.comodos.append(comodo)

    def listar_comodos(self):
        if not self.comodos:
            print("\nNenhum cômodo cadastrado.")
            return

        print("\nCômodos da residência:")
        for i, comodo in enumerate(self.comodos, 1):
            print(f"{i} - {comodo.nome}: {comodo.area:.2f} m²")

    def calcular_area_total(self):
        total = 0
        for comodo in self.comodos:
            total += comodo.area
        return total


def main():
    residencia = Residencia()

    while True:
        print("\n===== MINHA RESIDÊNCIA =====")
        print("1 - Adicionar cômodo")
        print("2 - Listar cômodos")
        print("3 - Calcular área total")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cômodo: ")

            try:
                area = float(input("Área do cômodo em m²: "))

                if area <= 0:
                    print("A área deve ser maior que zero.")
                    continue

                residencia.adicionar_comodo(nome, area)
                print("Cômodo adicionado com sucesso.")

            except ValueError:
                print("Digite uma área válida.")

        elif opcao == "2":
            residencia.listar_comodos()

        elif opcao == "3":
            total = residencia.calcular_area_total()
            print(f"\nÁrea total da residência: {total:.2f} m²")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

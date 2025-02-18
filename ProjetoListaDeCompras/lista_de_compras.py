# Lista de Compras em Python

def exibir_menu():
    print("\nMENU DE OPÇÕES:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Pesquisar produtos")
    print("4. Sair do programa")


def listar_produtos(lista):
    if not lista:
        print("\nA lista de compras está vazia.")
    else:
        print("\nLista de Compras:")
        for produto in lista:
            print(
                f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']} {produto['unidade']}, Descrição: {produto['descricao']}")


def adicionar_produto(lista, proximo_id):
    nome = input("Digite o nome do produto: ").strip()
    print("Escolha a unidade de medida:")
    unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    for i, unidade in enumerate(unidades, 1):
        print(f"{i}. {unidade}")

    while True:
        try:
            opcao_unidade = int(input("Digite o número correspondente à unidade: "))
            if 1 <= opcao_unidade <= len(unidades):
                unidade = unidades[opcao_unidade - 1]
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    while True:
        try:
            quantidade = float(input("Digite a quantidade: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    descricao = input("Digite uma descrição para o produto: ").strip()

    produto = {
        "id": proximo_id,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descricao": descricao
    }
    lista.append(produto)
    print(f"\nProduto '{nome}' adicionado com sucesso!")


def remover_produto(lista):
    try:
        id_remover = int(input("Digite o ID do produto que deseja remover: "))
        for produto in lista:
            if produto["id"] == id_remover:
                lista.remove(produto)
                print(f"Produto '{produto['nome']}' removido com sucesso!")
                return
        print("Produto com o ID especificado não encontrado.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")


def pesquisar_produtos(lista):
    termo = input("Digite o nome ou parte do nome do produto que deseja pesquisar: ").strip().lower()
    resultados = [produto for produto in lista if termo in produto["nome"].lower()]

    if not resultados:
        print("\nNenhum produto encontrado com o termo especificado.")
    else:
        print(f"\nForam encontrados {len(resultados)} produto(s):")
        for produto in resultados:
            print(
                f"ID: {produto['id']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']} {produto['unidade']}, Descrição: {produto['descricao']}")


def main():
    lista_de_compras = []
    proximo_id = 1


    while True:
        listar_produtos(lista_de_compras)
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto(lista_de_compras, proximo_id)
            proximo_id += 1
        elif opcao == "2":
            remover_produto(lista_de_compras)
        elif opcao == "3":
            pesquisar_produtos(lista_de_compras)
        elif opcao == "4":
            print("\nEncerrando o programa. Até a próxima!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()

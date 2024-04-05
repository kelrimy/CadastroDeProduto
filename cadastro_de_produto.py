#Requisito: 𝐂𝐚𝐝𝐚𝐬𝐭𝐫𝐨 𝐞 𝐥𝐢𝐬𝐭𝐚𝐠𝐞𝐦 𝐝𝐞 𝐩𝐫𝐨𝐝𝐮𝐭𝐨𝐬

#𝐂𝐚𝐝𝐚𝐬𝐭𝐫𝐨:

# - Formulário com os campos abaixo:
#
#   - Nome do produto - campo de texto
#   - Descrição do produto - campo de texto
#   - Valor do produto - campo de valor
#   - Disponível para venda - campo com 2 opções: sim / não
#
# 𝐋𝐢𝐬𝐭𝐚𝐠𝐞𝐦:
#
# - Colunas da listagem: nome, valor
# - Ordenação por valor do menor para o maior
# - Quando cadastrar um novo produto é para abrir a listagem automaticamente
# - Deve existir um botão para cadastrar um novo produto a partir da listagem

# Lista de produtos (inicialmente vazia)
produtos = []


def cadastrar_produto():
    while True:
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        valor = input("Digite o valor do produto: ")

        while True:
            # Tenta converter o valor para float
            try:
                valor = float(valor)
                break  # Se a conversão for bem sucedida, sai do loop
            except ValueError:
                print("Erro: O valor do produto deve ser numérico.")
                valor = input("Digite o valor do produto novamente: ")

        while True:
            disponivel = input("O produto está disponível para venda? (S/N): ").upper()

            # Verifica se a disponibilidade é válida
            if disponivel in ['S', 'N']:
                break
            else:
                print("Erro: Resposta inválida. Digite 's' ou 'n'.")

        # Adiciona o produto à lista de produtos
        produtos.append({'nome': nome, 'descricao': descricao, 'valor': valor, 'disponivel': disponivel})

        # Pergunta se deseja cadastrar outro produto
        while True:
            continuar = input("Deseja cadastrar outro produto? (S/N): ").upper()
            if continuar in ['S', 'N']:
                break
            else:
                print("Erro: Resposta inválida. Digite 'S' ou 'N'.")

        if continuar == 'N':
            break

def listar_produtos():
    print("\nListagem de Produtos")
    print("-" * 50)
    print(f"{'Nome':<20} {'Valor':<15} {'Disponível':<20}")
    print("-" * 50)
    for produto in produtos:
        nome = produto['nome']
        valor = f"R$ {produto['valor']:0.2f}"
        disponivel = produto['disponivel'].capitalize()
        print(f"{nome:<20} {valor:<15} {disponivel:<20}")
    print("-" * 50)


# Função principal
def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

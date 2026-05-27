
produtos = []
 
 
# 1. CREATE (Adicionar)
 
def adicionar_produto(nome):
    produtos.append(nome)
    print(f" Produto '{nome}' adicionado com sucesso!")
 
 
# 2. READ (Listar)
 
def listar_produtos():
    if not produtos:
        print("A lista de produtos está vazia.")
        return
 
    print("\n--- LISTA DE PRODUTOS ---")
    for i, nome in enumerate(produtos, start=1):
        print(f"{i}. {nome}")
    print("-------------------------")
 
# 3. UPDATE (Atualizar)
 
def atualizar_produto(nome_antigo, nome_novo):
    if nome_antigo in produtos:
        # Descobre a posição (índice) da primeira ocorrência do produto
        indice = produtos.index(nome_antigo)
        produtos[indice] = nome_novo
        print(f" Produto '{nome_antigo}' atualizado para '{nome_novo}'!")
    else:
        print(f" Erro: Produto '{nome_antigo}' não encontrado.")
 
 
# 4. DELETE (Deletar)
 
def deletar_produto(nome):
    if nome in produtos:
        produtos.remove(nome)
        print(f" Produto '{nome}' removido com sucesso!")
    else:
        print(f" Erro: Produto '{nome}' não encontrado.")
 
#Progama Principal
opcao = 0
opcao2 = 0
while(opcao not in ["n"]):
    opcao2 = 0
    while(opcao2 not in ["adicionar", "lista" "atualizar", "deletar",]):
        opcao2 = input("Opções para mexer com a lista: \n adicionar \n lista \n atualizar \n deletar \n O que deseja fazer?: ")
        print("")
        match(opcao2):
            case "adicionar":
                informacao = input("O que você quer adicionar a lista? \n Coloque algo pra adicionar na lista: ")
                adicionar_produto(informacao)
            case "lista":
                listar_produtos()
            case "atualizar":
                informacao = input("Qual o nome você quer atualizar: ")
                informacao2 = input("Qual vai ser o novo nome: ")
                atualizar_produto(informacao, informacao2)
            case "deletar":
                informacao = input("O que quer deletar na lista? \n")
                deletar_produto(informacao)
            case _:
                print("digitar novamente a mensagem.")
    opcao = input("Vai querer continuar na lista? s ou n\n")
    opcao = 0
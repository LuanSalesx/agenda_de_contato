from utils.cadastros.incluir import incluir_contato
from utils.cadastros.listar import listar_contato
from utils.cadastros.pesquisar import pesquisar_contatoID
from utils.cadastros.remover import remover_contato

def menu():
    opcao = input("Digite a opção desejada: ")
    print("Menu")
    print("1. Adicionar")
    print("2. Listar")
    print("3. Pesquisar por ID do contato")
    print("4. Remover")
    print("5. Sair")

    if opcao == '1':
        incluir_contato()
    elif opcao == '2':
        listar_contato()
    elif opcao == '3':
        pesquisar_contatoID()
    elif opcao == '4':
        remover_contato()
    elif opcao == '5':
        print("Saindo...")
# Funções do sistema

alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    idade = int(input("Digite a idade do aluno: "))
    lista_de_notas = []

    novo_aluno = {
        "nome": nome,
        "matricula": matricula,
        "idade": idade,
        "notas": lista_de_notas
    }

    alunos.append(novo_aluno)

def adicionar_nota():
    while True:
        id = int(input("Digite a matrícula do aluno: "))
        for aluno in alunos:
            if id == aluno['matricula']:
                while True:
                    nova_nota = float(input("Informe a nova nota do aluno: "))
                    aluno['notas'].append(nova_nota)
                    continuar = input("Você deseja inserir mais alguma nota? (S/N)").strip().upper()
                    if continuar in "N":
                        break
                    elif continuar in "S":
                        print(f"\nAdicionando nota ao aluno...")
            else:
                print(f"Valor incorreto tente novamente.")


def listar_alunos():
    print(f"\n\n{'=' * 30}\nLista de alunos \n{'=' * 30}")
    for aluno in alunos:
        print(f"Nome do aluno: {aluno['nome']} \nMatrícula do aluno: {aluno['matricula']} \nIdade do aluno: {aluno['idade']} \nNotas do aluno: {aluno['notas']}")





def iniciar():
    while True:
        inicio = int(input("\n\nEscolha uma opção: \n[ 1 ] - Cadastra aluno \n[ 2 ] - Adicionar nota \n[ 3 ] - Listar alunos \n[ 8 ] - Sair e salvar dados\n"))

        if inicio == 1:
            cadastrar_aluno()
        elif inicio == 2:
            adicionar_nota()
        elif inicio == 3:
            listar_alunos()
        elif inicio == 8:
            print("Saindo...")



# Funções do sistema

alunos = []

def cadastrar_aluno():
    nome = input("\nDigite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))

    for aluno in alunos:
        valor = matricula
        if matricula == aluno['matricula']:
            while matricula == aluno['matricula']:
                print("\nMatrícula já em uso, informe uma matrícula válida.")
                matricula = int(input("Digite a matrícula do aluno: "))

    idade = int(input("Digite a idade do aluno: "))
    lista_de_notas = []

    novo_aluno = {
        "nome": nome,
        "matricula": matricula,
        "idade": idade,
        "notas": lista_de_notas,
        "status": False
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
                        return
            else:
                print(f"Valor incorreto tente novamente.")
                return


def listar_alunos():
    print(f"\n\n{'=' * 30}\nLista de alunos \n{'=' * 30}")
    for aluno in alunos:
        print(f"Nome do aluno: {aluno['nome']} \nMatrícula do aluno: {aluno['matricula']} \nIdade do aluno: {aluno['idade']} \nNotas do aluno: {aluno['notas']} \n{'-' * 15}")


def atualizar_aluno():
    global alunos
    matricula = int(input("Informe a matrícula do aluno: "))
    for aluno in alunos:
        if matricula == aluno['matricula']:
            novo_nome = input("\nDigite o novo nome do aluno: ")
            novo_matricula = int(input("Digite a nova matrícula do aluno: "))
            novo_idade = int(input("Digite a nova idade do aluno: "))

            aluno['nome'] = novo_nome
            aluno['matricula'] = novo_matricula
            aluno['idade'] = novo_idade


def deletar_aluno():
    global alunos

    matricula = int(input("Informe a matrícula do aluno a ser excluída: "))
    
    for aluno in alunos:
        if matricula == aluno['matricula']:
            aluno['status'] = True

    alunos = [aluno for aluno in alunos if not aluno['status']]



def iniciar():
    while True:
        inicio = int(input("\n\nEscolha uma opção: \n[ 1 ] - Cadastra aluno \n[ 2 ] - Adicionar nota \n[ 3 ] - Listar alunos \n[ 4 ] - Atualizar dados do aluno \n[ 5 ] - Deletar aluno \n[ 6 ] - Sair e salvar dados\n"))

        if inicio == 1:
            cadastrar_aluno()
        elif inicio == 2:
            adicionar_nota()
        elif inicio == 3:
            listar_alunos()
        elif inicio == 4:
            atualizar_aluno()
        elif inicio == 5:
            deletar_aluno()
        elif inicio == 6:
            print("Saindo...")



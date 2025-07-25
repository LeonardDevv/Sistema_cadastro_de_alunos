import json
import os

alunos = []

if os.path.exists('alunos.json'):
    try:
        with open('alunos.json', 'r', encoding='utf8') as f:
            alunos = json.load(f)
    except Exception as e:
        print(f"Erro ao carregar os dados do arquivo alunos.json: {e}")


def cadastrar_aluno():
    nome = input("\nDigite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    for aluno in alunos:
        if matricula == aluno['matricula']:
            while matricula == aluno['matricula']:
                print("\nMatrícula já em uso, informe uma matrícula válida.")
                matricula = int(input("Digite a matrícula do aluno: "))
    idade = int(input("Digite a idade do aluno: "))
    lista_de_notas = []

    media = float()

    novo_aluno = {
        "nome": nome,
        "matricula": matricula,
        "idade": idade,
        "notas": lista_de_notas,
        "media": media,
        "status": False
    }
    alunos.append(novo_aluno)


def adicionar_nota():
    matricula = int(input("Digite a matrícula do aluno: "))
    id = int()
    for aluno in alunos:
            if matricula == aluno['matricula']:
                id = matricula
    if id != matricula:
                print("Matrícula não encontrada, tente novamente.")
                adicionar_nota()
    while True:
        for aluno in alunos:
            if id == aluno['matricula']:
                while True:
                    nova_nota = float(input("Informe a nova nota do aluno: "))
                    aluno['notas'].append(nova_nota)
                    continuar = input("Você deseja inserir mais alguma nota? (S/N)").strip().upper()
                    aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
                    if continuar in "N":
                        return


def listar_alunos():
    print(f"\n\n{'=' * 30}\nLista de alunos \n{'=' * 30}")
    for aluno in alunos:
        print(f"Nome do aluno: {aluno['nome']} \nMatrícula do aluno: {aluno['matricula']} \nIdade do aluno: {aluno['idade']} \nNotas do aluno: {aluno['notas']} \nMédia do aluno: {aluno['media']:.2f} \n{'-' * 30}")


def atualizar_aluno():
    global alunos
    matricula = int(input("Informe a matrícula do aluno: "))
    id = int()
    for aluno in alunos:
            if matricula == aluno['matricula']:
                id = matricula
    if id != matricula:
                print("Matrícula não encontrada, tente novamente.")
                atualizar_aluno()
    while True:
        for aluno in alunos:
            if matricula == aluno['matricula']:
                novo_nome = input("\nDigite o novo nome do aluno: ")
                novo_matricula = int(input("Digite a nova matrícula do aluno: "))
                novo_idade = int(input("Digite a nova idade do aluno: "))
                aluno['nome'] = novo_nome
                aluno['matricula'] = novo_matricula
                aluno['idade'] = novo_idade
                return


def deletar_aluno():
    global alunos
    matricula = int(input("Informe a matrícula do aluno a ser excluída: "))
    id = int()
    for aluno in alunos:
            if matricula == aluno['matricula']:
                id = matricula
    if id != matricula:
                print("Matrícula não encontrada, tente novamente.")
                deletar_aluno()
    while True:
        for aluno in alunos:
            if matricula == aluno['matricula']:
                print(f"\nAluno(a) {aluno['nome']} deletado.")
                aluno['status'] = True     
                alunos = [aluno for aluno in alunos if not aluno['status']]
                return


def iniciar():
    while True:
        inicio = int(input("\n\nEscolha uma opção: \n[ 1 ] - Cadastra aluno \n[ 2 ] - Adicionar nota \n[ 3 ] - Listar alunos \n[ 4 ] - Atualizar dados do aluno \n[ 5 ] - Deletar aluno \n[ 6 ] - Salvar dados em .txt \n[ 7 ] - Sair e salvar dados\n"))
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
            try:
                 with open('alunos.txt', 'w', encoding='utf8') as s:
                      json.dump(alunos, s, ensure_ascii=False, indent=4)
                      print("Dados salvos com sucesso em alunos.txt")
            except Exception as e:
                 print(f"Ocorreu um erro ao salvar os dados: {e}")
        elif inicio == 7:
            print("Salvando dados e saindo...")
            try:
                with open('alunos.json', 'w', encoding='utf8') as f:
                    json.dump(alunos, f, ensure_ascii=False, indent=4)
                    print("Dados salvos com sucesso em alunos.json")
            except Exception as e:
                print(f"Ocorreu um erro ao salvar os dados: {e}")

    
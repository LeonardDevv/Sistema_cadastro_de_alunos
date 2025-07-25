# 🏫 Sistema de Cadastro de Alunos (Python)
Um sistema simples, com interface em terminal, para cadastrar, listar, atualizar e remover alunos com notas. Ideal para fins de aprendizado em Python e manipulação básica de dados. </br>

### ⚙️ Funcionalidades
- Cadastro de alunos (nome, matrícula, idade e notas).
- Adição de notas para alunos existentes.
- Listagem de todos os alunos e suas informações.
- Validação básica de entrada para evitar erros ou duplicidade.
- Persistência de dados opcional via arquivo JSON (se aplicado).
- Arquitetura em módulos separados (core.py, main.py), facilitando manutenção e escalabilidade.

### 🚀 Como rodar localmente

1. Clone o repositório
```bash
git clone https://github.com/LeonardDevv/Sistema_cadastro_de_alunos.git
cd Sistema_cadastro_de_alunos
```

2. Execute o arquivo principal:
```bash
python main.py
```

3. Siga as instruções no terminal para cadastrar alunos, adicionar notas, listar ou encerrar o programa.

### 🧩 Organização do Projeto
| Arquivo   | Descrição                                                              |
| --------- | ---------------------------------------------------------------------- |
| `main.py` | Controla o loop principal e carrega os dados                           |
| `core.py` | Contém funções como cadastrar, adicionar nota, listar e iniciar o menu |

### 🧠 Fluxo de Funcionamento
1. main.py inicia o programa e chama core.iniciar().
2. core.iniciar() exibe o menu com opções disponíveis.
3. Usuário escolhe a operação desejada (ex: cadastrar, adicionar nota).
4. Funções específicas em core.py processam as entradas e manipulam a lista alunos.
5. Ao encerrar, os dados podem ser salvos externamente (se implementado).

### 🎯 Quem deve usar?
Esse projeto é excelente para quem está aprendendo Python e quer aplicar:
- Lógica de controle com loops e condicionais.
- Uso de listas e dicionários.
- Modularização e boas práticas de código.
- Fundamentos de entrada e saída no terminal.

### 🖋️ Mensagem final
Se quiser evoluir o projeto, você pode adicionar:
- Uma interface visual.
- Tratamentos adicionais de exceção e validação.
- Histórico de alterações.


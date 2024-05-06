import json
opc = None
verLista = list()
def adicionarAluno():
        Nome = input('Digite o nome do Aluno: ')
        Idade = input('Digite a Idade do Aluno: ')
        Nascimento = input('Digite o ano de Nasciemnto do ALuno: ')
        verLista.append(dict(Nome=Nome, Idade=Idade,Nasciemnto=Nascimento))
        with open('TesteNasci.json', 'w') as prox:
                json.dump(verLista,prox, indent='\t')
        print("Aluno adicionado com sucesso!")

def olharLista():
        with open('TesteNasci.json','r') as prox:
            verLista = json.load(prox)
        print(verLista)

def pesquisar_aluno(nome):
    with open('TesteNasci.json', 'r') as prox:
        verLista = json.load(prox)
    for aluno in verLista:
        if nome == aluno['Nome']:
            print(f"A idade do aluno {nome} com a Idade de {aluno['Idade']} nascido no ano de {aluno['Nasciemnto']}")
            break
    else:
        print(f"O aluno {nome} não foi encontrado.")

while opc != 'term':
    opc = input('''
    Você deseja ver lista ou adicionar algo a lista ou sair?
    Selecione:
    add para Adicionar
    ver para Ver Lista de Adicionados 
    pesq para Pesquisar Aluno
    term para Terminar
    Escolha aqui: 
    ''')
    if opc == 'add':
        adicionarAluno()
    elif opc == 'ver':
        olharLista()
    elif opc == 'pesq':
        nome_pesquisar = input("Digite o nome do aluno que deseja pesquisar: ")
        pesquisar_aluno(nome_pesquisar)
    else:
        print('Opção digita não é a correta')

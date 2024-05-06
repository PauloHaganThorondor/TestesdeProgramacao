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

while opc != 'term':
    opc = input('''
    Você deseja ver lista ou adicionar algo a lista ou sair?
    Selecione:
    add para Adicionar
    ver para Ver Lista de Adicionados 
    term para Terminar
    Escolha aqui: 
    ''')
    if opc == 'add':
        adicionarAluno()
    elif opc == 'ver':
        olharLista()

    else:
        print('Opção digita não é a correta')
    '''veri = input('Deseja Verificar se aluno está cadastrado? s ou n:')
    if veri == 's':
        with open('TesteNasci.json', 'r') as prox:
            verLista = json.load(prox)
        nomepes = input('Nome do Aluno para ser pesquisado: ')
         if nomepes == verLista.appendd(dict(Nome)):
            print(verLista)'''

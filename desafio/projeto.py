from desafio import quero_curso as qc
from time import sleep

if not qc.verificarArquivo('cadastro.txt'): #Verifica se o arquivo 'cadastro.txt' existe
    qc.criarArquivo('cadastro.txt', 'cpf;telefone;e-mail;senha') #Cria o arquivo caso o mesmo não já tenha sido criado

qc.cabeçalho('SUPERMERCADO ABA')
print('''
[1] - Fazer Login
[2] - Fazer Cadastro
''')
while True:
    try:
        opção = int(input('Opção: '))
    except:
        print(' -Digite um número inteiro válido-')
        continue
    else:
        if opção < 1 or opção > 2:
            print(' -Digite uma opção válida-')
            continue
        else:
            break

while opção < 1 or opção > 2:
    print('\tDigite 1 ou 2')
    opção = int(input('Opção: '))

if opção == 2:
    qc.cabeçalho("CADASTRO")
    cpf = qc.pegarCPF() #A partir daqui váriaveis globais recebem o retorno das funções correspondentes
    tell = qc.pegarTelefone()
    email = qc.pegarEmail()
    senha = qc.pegarSenha() #Fim da atribuição dessas váriaveis
    qc.adicionarNoArquivo(f'{cpf};{tell};{email};{senha}', 'cadastro.txt') #Adiciona no arquivo 'cadastro.txt' os dados, dividos por ';'.
    print('-- Cadastro Finalizado --')
    print('    Redirecionando...')
    sleep(2)

qc.cabeçalho('LOGIN')
email_login = qc.pegarEmail(False)
senha_login = qc.pegarSenha()
login = qc.realizarLogin(email_login, senha_login, 'cadastro.txt') #Análise da correspondência do e-mail e senha com os já armazenados

if login:
    qc.cabeçalho('ÁREA DE COMPRAS')
    print('''Modos de exibição:
  [1] - Do mais barato ao mais caro.
  [2] - Do mais caro ao mais barato.
  [3] - Ordem de código dos produtos.''')
    while True:
        try:
            opção = int(input('Opção: '))
        except:
            print('>>Digite um número inteiro<<')
            continue
        else:
            if opção < 1 or opção > 3:
                print('Opção não correspondente, tente novamente.')
                continue
            else:
                print('', '_' * 81)
                if opção == 1:
                    qc.ordenarProdutos(crescente=True)
                elif opção == 2:
                    qc.ordenarProdutos(crescente=False)
                else:
                    qc.ordenarProdutos(ord_de_cód=True)
                print('', '-' * 81)
        break

lista_compras = qc.compras('produtos.txt')
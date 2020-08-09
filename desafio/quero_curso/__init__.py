def verificarArquivo(nome_do_arquivo=''):
    '''
    --> Responsável pela verificação da existência de um arquivo.
    :param nome_do_arquivo: É passado o nome do arquivo juntamente com sua extensão.
    :return: Se o arquivo não existir, retorna False. Caso exista, retorna True.
    '''

    try:
       arq = open(nome_do_arquivo, 'rt')
       arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_do_arquivo='', primeira_linha=''):
    '''
    --> Responsável pela criação de um arquivo.
    :param nome_do_arquivo: É passado o nome do arquivo juntamente com sua extensão.
    :return: Sem retorno
    '''

    try:
       arq = open(nome_do_arquivo, 'wt+')
       arq.write(primeira_linha + '\n')
       arq.close()
    except:
        print('Não foi possível criar o arquivo')
    else:
        print(f'Arquivo "{nome_do_arquivo}" criado')


def adicionarNoArquivo(inf_para_adicionar='', nome_do_arquivo=''):
    '''
    --> Responsável por adicionar informações no arquivo.
    :param inf_para_adicionar: Informações que serão adicionadas.
    :param nome_do_arquivo: Nome do arquivo juntamente com sua extensão.
    :return: Sem retorno.
    '''
    arq = open(nome_do_arquivo, 'at')
    arq.write(inf_para_adicionar + '\n')
    arq.close()


def cabeçalho(frase=''):
    '''
    --> Cria um cabeçalho com uma frase centralizada.
    :param frase: Frase a ser exibida.
    :return: Sem retorno.
    '''
    print('-' * (len(frase) + 20))
    print(' ' * 9, frase)
    print('-' * (len(frase) + 20))


def pegarTelefone():
    '''
    --> Responsável por receber e padronizar visualmente o DDD e Número Telefonico.
    :return: Retorna a padronização telefonica (XX)xxxxx-xxxx.
    '''
    while True:
        try:
            ddd = str(input('DDD: ')).strip()
        except:
            print('\tDado inválido')
            continue
        else:
            if len(ddd) != 2:
                print('\tDDD é composto por dois dígitos')
                continue
            if not ddd.isnumeric():
                print('\tApenas números são válidos')
                continue
            else:
                while True:
                    try:
                        telefone = str(input('Telefone: ')).strip()
                    except:
                        print('\tDado inválido')
                        continue
                    else:
                        if not telefone.isnumeric():
                            print('\tDigite apenas números')
                            continue
                        if len(telefone) != 9:
                            print('\tO padrão telefônico é composto por 9 digitos')
                            continue
                    break
        ddd = f'({ddd})'#Padroniza o DDD colocando entre parentêses.
        lista = []
        for num in telefone:
            lista.append(num) #Adiciona na lista número a número como elementos separados.
        lista.insert(5, '-') #Padroniza com o hífen '-' na posição correta.
        telefone = ddd + ''.join(lista) #Atribui na váriavel a forma padronizada de DDD + Número telefonico.
        if análiseDeRepetição(telefone, 1, 'cadastro.txt') is True: #Função para análise de repetição com números já armazenados.
            print('-- O Nº de Telefone passado já foi cadastrado, tente novamente --')
            continue
        return telefone


def pegarCPF():
    '''
    --> Recebe a númeração do CPF e organiza utilizando pontos e hífen.
    :return: Retorna a padronização do CPF (xxx.xxx.xxx-xx).
    '''
    while True:
        try:
            cpf = str(input('CPF: ')).strip()
        except:
            print('\tDado inválido')
            continue
        else:
            if '.' in cpf or '-' in cpf:
                print('\tPreencha somente com a numeração')
                continue
            if not cpf.isnumeric():
                print('\tPreencha somente com a numeração')
                continue
            if len(cpf) != 11:
                print('\tPreencha o CPF corretamente com 11 algarismos')
                continue
            else:
                lista = []
                for elementos in cpf:
                    lista.append(elementos) #Insere na lista cada número passado de modo separado.
                lista.insert(3, '.') #Coloca a primeira pontução após os 3 primeiros dígitos.
                lista.insert(7, '.') #Coloca a segunda pontuação após os 6 primeiros dígitos.
                lista.insert(11, '-') #Coloca o hífen após os 9 primeiros digítos.
                cpf = ''.join(lista) #Atribui na variavel a forma padronizada.
                if análiseDeRepetição(cpf, 0, 'cadastro.txt') is True:
                    print('-- O CPF passado já foi cadastrado, tente novamente --')
                    continue
                else:
                    return cpf


def pegarEmail(cadastro=True):
    while True:
        try:
            email = str(input('E-mail: ')).strip()
        except:
            print('\tDado inválido')
            continue
        else:
            if '@' not in email:
                print('\tE-mail inválido. Tente novamente.')
                continue
            if '.' not in email:
                print('\tE-mail inválido. Tente novamente.')
                continue
            if cadastro is True:
                if análiseDeRepetição(email, 2, 'cadastro.txt') is True:
                    print('-- O E-mail passado já foi cadastrado, tente novamente --')
                    continue
            return email
        break


def pegarSenha():
    while True:
        try:
            senha = str(input('Senha: ')).strip()
        except:
            print('\tDado inválido')
            continue
        else:
            if len(senha) < 7:
                print('A senha deve ter no mínimo 7 digitos')
                continue
            if not senha.isalnum():
                print('A senha só pode conter números e letras')
                continue
            return senha
        break


def análiseDeRepetição(informação, posição, nome_do_arquivo=''):
    '''
    ->Faz uma análise da informação passa com as já cadastradas para verificar repetições.
    :param informação: A informação que será analisada.
    :param posição: A posição no arquivo que está o conjunto de dados do mesmo tipo.
    :param nome_do_arquivo: Nome do arquivo.txt a ser aberto.
    :return: Retorna False para caso o arquivo esteja vazio ou não haja repetição. Retorna True caso haja repetição.
    '''
    arq = open(nome_do_arquivo, 'rt')
    arq.readline()
    for linhas in arq:
        if linhas == '':
            return False
        if informação == linhas.split(';')[posição]: #Comparação da informação com a coluna especificada de dados do arquivo.
            return True
        else:
            return False


def realizarLogin(pos1, pos2, login1='', login2='', nome_do_arquivo=''):
    '''
    ->Verifica o login do usuário, com base nos dados passados e os que estão cadastrados.
    :param pos1: Posição no arquivo do primeiro elemento de verificação.
    :param pos2: Posição no arquivo do segundo elemento de verificação.
    :param login1: Primeiro elemento para efetuação do login. Ex: e-mail, código de login e etc...
    :param senha: Segundo elemento para efetuação do login. Ex: Senhas, códigos e etc...
    :param nome_do_arquivo: Nome do arquivo com sua extensão a ser analisado.
    :return: Caso haja correspondência das informações, logo havendo login, retorna True. Senão, retorna False.
    '''
    arq = open(nome_do_arquivo, 'rt')
    arq.readline()
    tupla = (login1, login2)
    lista = []
    for linhas in arq:
        tupla_dados = (linhas.split(';')[pos1], linhas.split(';')[pos2].replace('\n', '')) #Pega as informações das possições passadas do arquivo, colocando eles em uma tupla.
        lista.append(tupla_dados)
    if tupla in lista: #Verifica se a tupla contendo os dados passados consta na lista com as tuplas de dados cadastrados.
        print('-- Login efetuado --')
        return True
    else:
        print('~Não há conta com estas informações~')
        return False


def ordenarProdutos(ord_de_cód=False, crescente=True):
    '''
    ->Realiza a ordenação com base nos preços ou códigos dos produtos contidos no arquivo "produtos.txt".
    :param ord_de_cód: Caso True, irá ordenar por código. Caso False, permite a ordenação por preço.
    :param crescente: Caso True, irá ordenar do mais barato ao mais caro. Caso False, ordena do mais caro ao mais barato.
    :return: Sem retorno.
    '''
    lista = []
    lista_produtos = []
    with open("produtos.txt", "r", encoding="utf8") as arquivo:
        arquivo.readline()
        for produto in arquivo:
            lista.append(produto.split(";"))
        for linha in lista:
            lista_produtos.append({"codigo": linha[0], "produto": linha[1], "preço": float(linha[2]), "estoque": int(linha[3])})
    if ord_de_cód is False:
        if crescente:
            lista_ordenada = []
            while not lista_produtos == []:
                menor_preço = lista_produtos[0]["preço"]
                for produto in lista_produtos:
                    if produto["preço"] < menor_preço:
                        menor_preço = produto["preço"]
                for produto in lista_produtos:
                    if produto["preço"] == menor_preço:
                        lista_ordenada.append(produto)
                        lista_produtos.remove(produto)
        else:
            lista_ordenada = []
            while not lista_produtos == []:
                menor_preço = lista_produtos[0]["preço"]
                for produto in lista_produtos:
                    if produto["preço"] > menor_preço:
                        menor_preço = produto["preço"]
                for produto in lista_produtos:
                    if produto["preço"] == menor_preço:
                        lista_ordenada.append(produto)
                        lista_produtos.remove(produto)

        for produto in lista_ordenada:
            print(f"| Codigo: {produto['codigo']}     Produto: {produto['produto']:<18}", f"Preço: R${float(produto['preço']):<10.2f}".replace('.', ','), f"Estoque: {produto['estoque']:<5}", f"{'|':<1}")
    else:
        for produto in lista_produtos:
            print(f"| Codigo: {produto['codigo']}     Produto: {produto['produto']:<18}", f"Preço: R${float(produto['preço']):<10.2f}".replace('.', ','), f"Estoque: {produto['estoque']:<5}", f"{'|':<1}")


def compras(nome_do_arquivo=''):
    '''
    ->Sistema de compras para análise do produto escolhido, quantidade a ser comprada e então alterar no armazenamento a quantidade do estoque.
    :param nome_do_arquivo: Nome do arquivo com sua extensão.
    :return: Retorna uma lista com dicionários que contém as informações de compra de cada produto escolhido.
    '''
    org = {} #Dicionário que irá conter as informações da compra de um produto.
    lista_geral = [] #Lista que irá conter os dicionários de cada produto da compra.
    cód_produtos = [] #Lista que irá armazenar os códigos de todos os produtos da loja.
    cód_usados = [] #Lista que armazena os códigos já usados, para analise de repetições.
    inf_do_arq = [] #Lista que irá conter as informações do arquivo, para sua modificação com base na compra.
    try:
        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
            arq.readline()
            for linhas in arq:
                cód_produtos.append(linhas.split(';')[0]) #Passa todos os códigos de produto para a lista.
    except:
        print('-- Não foi possível a leitura do arquivo de produtos --')
    else:

        while True:
            repetição = False #Variável para análise de repetição.
            sem_estoque = False #Variável para análise de produtos com estoque 0.
            try:
                código = str(input('Código do produto: ')).strip() #Código do produto que será comprado.
            except:
                print('-- Digite uma numeração composta por 4 digitos --')
                continue
            else:
                if not código.isnumeric(): #Verifica se é composto por somente números.
                    print('-- O código dos produtos são compostos somente por números --')
                    continue
                if código not in cód_produtos: #Verifica se o código se encontra entre os códigos de produtos.
                    print('-- O código digitado não corresponde a um produto --')
                    continue
                else:
                    if código not in cód_usados: #Verifica se o código não foi usado antes, para criação de um novo dicionário.
                        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
                            arq.readline()
                            for linhas in arq:
                                if código == linhas.split(';')[0]: #Verifica qual o produto escolhido.
                                    if int(linhas.split(';')[3]) == 0: #Verifica se está sem estoque.
                                        sem_estoque = True #Caso estoque seja 0, a variável recebe True.
                                        print('-- No momento estamos com falta do produto --')
                                        break
                                    else: #Se houver estoque, passa informações para o dicionário.
                                        org['produto'] = linhas.split(';')[1]
                                        org['código'] = linhas.split(';')[0]
                                        org['preçoUnidade'] = float(linhas.split(';')[2])
                                        org['estoque'] = int(linhas.split(';')[3])
                                        cód_usados.append(código)
                            if sem_estoque: #Caso a variável seja True, verifica se o cliente deseja continuar a compra.
                                perg = str(input('Quer continuar a compra?[S/N] ')).strip().upper()[0]
                                while perg not in 'SN':
                                    print('Digite SIM ou NÃO')
                                    perg = str(input('Quer continuar a compra?[S/N] ')).strip().upper()[0]
                                if perg == 'S':
                                    continue
                                else:
                                    break
                    else:
                        repetição = True #Caso o código esteja na lista de já usados, a var recebe True.

            while True:
                try:
                    quantidade = int(input('Quantidade a ser comprada:')) #Quantidade do produto a ser comprada.
                except:
                    print('Dado inválido')
                    continue
                else:
                    if not repetição: #Verifica se a var de repetição é False.
                        org['quantidade'] = quantidade #Não sendo repetição, adiciona informação no dicionário.
                        if org['quantidade'] > org['estoque']: #Verifica se a quantidade excede o estoque do produto.
                            print(f'-- A quantia excede o estoque de {org["estoque"]} {org["produto"]} --')
                            continue
                        else:
                            org['estoque'] -= org['quantidade'] #Se não exceder, refaz o estoque com a subtração da quantidade comprada.
                            org["preçoTot"] = org['quantidade'] * org['preçoUnidade'] #Adiciona no dicionário o preço total de compra daquele produto.
                            lista_geral.append(org.copy()) #Manda para a lista que irá conter todos os dicionários, uma cópia das informações.
                    else:
                        for num, dicionários in enumerate(lista_geral): #Percorre a lista, pegando seus índices e dicionários.
                            if dicionários['código'] == código: #Verifica em qual dicionário está a correspondência de código.
                                if quantidade <= dicionários['estoque']: #Verifica se a quantidade não excede o estoque do produto.
                                    lista_geral[num]['quantidade'] += quantidade #Adiciona nas informações já existentes daquele produto, a quantidade a mais a ser comprada.
                                    lista_geral[num]['preçoTot'] += quantidade * lista_geral[num]['preçoUnidade'] #Adiciona no preço total a quantia com base na quantidade comprada.
                                    lista_geral[num]['estoque'] -= quantidade #Refaz o estoque do produto, subtraindo novamente com a quantidade a mais comprada.
                                else:
                                    print(f'-- A quantidade excede o estoque de {lista_geral[num]["estoque"]} {lista_geral[num]["produto"]}')
                break
            perg = str(input('Deseja realizar mais uma compra?[S/N] ')).strip().upper()[0]
            while perg not in 'SN':
                print('Digite SIM ou NÃO')
                perg = str(input('Deseja realizar mais uma compra?[S/N] ')).strip().upper()[0]
            if perg == 'S': #Verifica se quer fazer mais uma compra, caso 'S', volta para o mesmo processo.
                continue
            else: #Não querendo realizar mais uma compra, é encerrado o processo.
                break

        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq: #Lê o arquivo.
            arq.readline()
            for linhas in arq:
                inf_do_arq.append(linhas) #Passa para a lista cada linha do arquivo.
        with open(nome_do_arquivo, 'wt+', encoding='utf8') as arq: #Cria um novo arquivo de mesmo nome.
            arq.write('código;produto;preço;estoque' + '\n')  #Digita a primeira linha de organização.
        with open(nome_do_arquivo, 'at', encoding='utf8') as arq: #Abre o arquivo récem criado, para incremento de informação.
            for linhas in inf_do_arq: #Percorre a lista com as linhas do arquivo apagado e recriado.
                if lista_geral == []:
                    arq.write(linhas) #Caso não tenha sido feita uma compra, ele repassa as informações sem alteração.
                else:
                    for dicionários in lista_geral: #Percorre os dicionários contidos na lista.
                        if linhas.split(';')[0] == dicionários['código']: #Verifica se algum código das linhas armazenadas é igual a algum código de compra armazenado.
                            correção = linhas.split(';') #Cria a var correção, para modificar o arquivo com base nas compras feitas.
                            correção[3] = str(dicionários['estoque']) #Refaz o estoque do arquivo com base no estoque alterado pela compra.
                            arq.write(';'.join(correção) + '\n') #Envia a alteração para o arquivo.
                        else:
                            arq.write(linhas) #Não havendo igualdade com algum código de compra, envia para o arquivo informações sem alterações.
    return lista_geral #Retorna a lista que contém todos os dados de compra dos produtos.

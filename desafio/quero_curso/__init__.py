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


def realizarLogin(email='', senha='', nome_do_arquivo=''):
    '''
    ->Verifica se os dados passados constam no arquivo de cadastro para uma efetuação do login.
    :param email: Recebe o e-mail passado na área de login.
    :param senha: Recebe a senha passada na área de login.
    :param nome_do_arquivo: Nome do arquivo.txt a ser analisado.
    :return: Retorna True no caso dos dados passados estarem cadastrados e False caso não estejam.
    '''
    arq = open(nome_do_arquivo, 'rt')
    arq.readline()
    tupla = (email, senha)
    lista = []
    for linhas in arq:
        tupla_dados = (linhas.split(';')[2], linhas.split(';')[3].replace('\n', '')) #Pega os e-mails e senhas do arquivo, colocando eles em uma tupla.
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


def compras(nome_do_arquivo='', definidor_de_retorno = True):
    org = {}
    lista_geral = []
    cód_produtos = []
    cód_usados = []
    inf_do_arq = []
    try:
        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
            arq.readline()
            for linhas in arq:
                cód_produtos.append(linhas.split(';')[0])
    except:
        print('-- Não foi possível a leitura do arquivo de produtos --')
    else:

        while True:
            repetição = False
            sem_estoque = False
            try:
                código = str(input('Código do produto: ')).strip()
            except:
                print('-- Digite uma numeração composta por 4 digitos --')
                continue
            else:
                if not código.isnumeric():
                    print('-- O código dos produtos são compostos somente por números --')
                    continue
                if código not in cód_produtos:
                    print('-- O código digitado não corresponde a um produto --')
                    continue
                else:
                    if código not in cód_usados:
                        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
                            arq.readline()
                            for linhas in arq:
                                if código == linhas.split(';')[0]:
                                    if int(linhas.split(';')[3]) == 0:
                                        sem_estoque = True
                                        print('-- No momento estamos com falta do produto --')
                                        break
                                    else:
                                        org['produto'] = linhas.split(';')[1]
                                        org['código'] = linhas.split(';')[0]
                                        org['preçoUnidade'] = float(linhas.split(';')[2])
                                        org['estoque'] = int(linhas.split(';')[3])
                                        cód_usados.append(código)
                            if sem_estoque:
                                perg = str(input('Quer continuar a compra?[S/N] ')).strip().upper()[0]
                                while perg not in 'SN':
                                    print('Digite SIM ou NÃO')
                                    perg = str(input('Quer continuar a compra?[S/N] ')).strip().upper()[0]
                                if perg == 'S':
                                    continue
                                else:
                                    break
                    else:
                        repetição = True

            while True:
                try:
                    quantidade = int(input('Quantidade a ser comprada:'))
                except:
                    print('Dado inválido')
                    continue
                else:
                    if not repetição:
                        org['quantidade'] = quantidade
                        if org['quantidade'] > org['estoque']:
                            print(f'-- A quantia excede o estoque de {org["estoque"]} {org["produto"]} --')
                            continue
                        else:
                            org['estoque'] -= org['quantidade']
                            org["preçoTot"] = org['quantidade'] * org['preçoUnidade']
                            lista_geral.append(org.copy())
                    else:
                        for num, dicionários in enumerate(lista_geral):
                            if dicionários['código'] == código:
                                if quantidade <= dicionários['estoque']:
                                    lista_geral[num]['quantidade'] += quantidade
                                    lista_geral[num]['preçoTot'] += quantidade * lista_geral[num]['preçoUnidade']
                                    lista_geral[num]['estoque'] -= quantidade
                                else:
                                    print(f'-- A quantidade excede o estoque de {lista_geral[num]["estoque"]} {lista_geral[num]["produto"]}')
                break
            perg = str(input('Deseja realizar mais uma compra?[S/N] ')).strip().upper()[0]
            while perg not in 'SN':
                print('Digite SIM ou NÃO')
                perg = str(input('Deseja realizar mais uma compra?[S/N] ')).strip().upper()[0]
            if perg == 'S':
                continue
            else:
                break

        with open(nome_do_arquivo, 'rt', encoding='utf8') as arq:
            arq.readline()
            for linhas in arq:
                inf_do_arq.append(linhas)
        with open(nome_do_arquivo, 'wt+', encoding='utf8') as arq:
            arq.write('código;produto;preço;estoque' + '\n')
        with open(nome_do_arquivo, 'at', encoding='utf8') as arq:
            for linhas in inf_do_arq:
                if lista_geral == []:
                    arq.write(linhas)
                else:
                    for dicionários in lista_geral:
                        if linhas.split(';')[0] == dicionários['código']:
                            correção = linhas.split(';')
                            correção[3] = str(dicionários['estoque'])
                            arq.write(';'.join(correção) + '\n')
                        else:
                            arq.write(linhas)
    return lista_geral

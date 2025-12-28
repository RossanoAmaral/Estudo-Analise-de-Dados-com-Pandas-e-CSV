import pandas as pd
from colorama import Fore, Style

def texto(msg='LEITURA DE DADOS CSV'):
    print('-'*42)
    print(msg.center(42))
    print('-'*42)
    return


def linha(tam=42):
    return print('-'*tam)


def opc_tabela(num):
    while True:
        try:
            op = int(input(num))
        except (ValueError,TypeError):
            texto(Fore.RED + 'ERRO AO LER OPÇÃO, DIGITE NOVAMENTE' + Style.RESET_ALL)
            continue
        else:
            break
    return op


def opc_tabela_vendas(num=4):
    while True:
        try:
            op_v = int(input(num))
        except (ValueError, TypeError):
            texto(Fore.RED + 'ERRO AO LER OPÇÃO, DIGITE NOVAMENTE' + Style.RESET_ALL)
            continue
        else:
            break
    return op_v



arquivo = 'tabela_dados.csv'
df = pd.read_csv(arquivo)

while True:
    texto()
    print(
    f"""
    [ 0 ] - Ler todos os dados
    [ 1 ] - Ler Produtos
    [ 2 ] - Quantidade de vendas
    [ 3 ] - Ler Preços
    [ 4 ] - Categoria
    [ 5 ] - Sair da tabela
    """
    )
    linha()

    opc = opc_tabela(Fore.GREEN + '>>> Digite sua opção: ' + Style.RESET_ALL)
    linha()

    while True:
        if opc > 5:
            opc = opc_tabela(Fore.RED + '>>> OPÇÃO INVÁLIDA, Digite apenas [0/5]: ' + Style.RESET_ALL)
            continue
        else:
            break

    if opc == 0:
        print(df)

    elif opc == 1:
        print(df['Produto'])

    elif opc == 2:
        print(df['Vendas'])
        linha()
        print(
        f"""
        [ 0 ] - Somar todas as vendas!
        [ 1 ] - Qual vendeu mais?
        [ 2 ] - Qual menos vendeu?
        [ 3 ] - Qual a média de vendas?
        [ 4 ] - Sair da tabela
        """
        )
        linha()
        opc_vendas = opc_tabela_vendas(Fore.GREEN + '>>> Digite sua opção para calcular vendas: ' + Style.RESET_ALL)
        while True:
            if opc_vendas >= 4:
                opc_vendas = opc_tabela_vendas(Fore.RED + '>>> OPÇÃO INVÁLIDA, Digite novamente: ' + Style.RESET_ALL)
                continue
            else:
                break
        if opc_vendas == 0:
            print(f'>>> A soma de todas as vendas são {df["Vendas"].sum()}!')
        
        elif opc_vendas == 1:
            print(f'>>> O produto que mais vendeu foi de {max(df["Vendas"])}')
        
        elif opc_vendas == 2:
            print(f'>>> O produto que menos vendeu foi de {min(df["Vendas"])}')
        
        elif opc_vendas == 3:
            print(f'>>> A média de vendas foi de {max(df["Vendas"]) / len(df["Vendas"])}')

    elif opc == 3:
        print(df['Preço'])

    elif opc == 4: 
        print(df['Categoria'])

    else:
        if opc == 5:
            break

texto('PROGRAMA ENCERRADO')
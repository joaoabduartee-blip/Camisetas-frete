print("Olá, Seja bem-vindo à loja Joao Pedro A.B Duarte.")


# Função do modelo [EXIGÊNCIA DE CÓDIGO 2 de 7]
def escolha_modelo():
    while True:
        modelo = input('Digite o modelo desejado (MCS/MLS/MCE/MLE): ').upper()
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else:
            print('Modelo inválido. Digite MCS, MLS, MCE ou MLE.')


# Função para número de camisetas [EXIGÊNCIA DE CÓDIGO 3 de 7]
def num_camiseta():
    while True:
        try:
            quantidade = int(input('Digite o número de camisetas: '))
            if quantidade > 20000:
                print('Não aceitamos pedidos acima de 20000 camisetas.')
                continue
            elif quantidade >= 2000:
                return quantidade * 0.88
            elif quantidade >= 200:
                return quantidade * 0.93
            elif quantidade >= 20:
                return quantidade * 0.95
            else:
                return quantidade
        except ValueError:
            print('Digite um valor numérico válido.')


# Função do frete [EXIGÊNCIA DE CÓDIGO 4 de 7]
def frete():
    while True:
        try:
            opcao = int(input('Escolha o frete (0-Retirar na fábrica, 1-Transportadora, 2-Sedex): '))
            if opcao == 0:
                return 0
            elif opcao == 1:
                return 100
            elif opcao == 2:
                return 200
            else:
                print('Opção inválida. Digite 0, 1 ou 2.')
        except ValueError:
            print('Digite um valor numérico válido.')


# Função dentro do principal - utilizando o try [EXIGÊNCIA DE CÓDIGO 5 de 7] e [EXIGÊNCIA DE CÓDIGO 6 de 7]
try:
    valor_modelo = escolha_modelo()
    quantidade_desconto = num_camiseta()
    valor_frete = frete()
   
    total = (valor_modelo * quantidade_desconto) + valor_frete
   
    print()
    print('Resumo do Pedido:')
    print(f'Valor unitário: R$ {valor_modelo:.2f}')
    print(f'Quantidade com desconto: {quantidade_desconto:.0f}')
    print(f'Frete: R$ {valor_frete:.2f}')
    print(f'Total a pagar: R$ {total:.2f}')


except Exception as e:
    print(f'Ocorreu um erro: {e}')


input("Pressione Enter para sair...")
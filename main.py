saldo=0
operacao=0
saques=[]
depositos=[]
extrato=[]
limite=500
numero_saques=3
LIMITE_SAQUES=3

def depositar(valor):
    globals()['saldo'] = globals()['saldo'] + valor
    depositos.append(valor)
    print(f'Saldo final: R$ {str(saldo).format(5.2)}')
    extrato.append([f'Depósito no valor de {valor:.2f}'])

def sacar(valor):
    if valor>globals()['saldo']:
        print("Saldo insuficiente")
    else:
        if len(saques) < numero_saques:
            if (sum(saques) + valor) >= limite:
                print("Limite diário ultrapassado")
            else:
                globals()['saldo'] = globals()['saldo'] - valor
                saques.append(valor)
                print(f'Saldo final: R$ {str(saldo).format(5.2)}')
                extrato.append([f'Saque no valor de {valor:.2f}'])
        else:
            print('Quantidade de saques diários alcançada')

def movimentar(operacao,valor):
    if operacao=='depositar':
        depositar(valor)
    if operacao=='sacar':
        sacar(valor)

def imprimeExtrato():
    if len(extrato) == 0:
        print("Sem movimentações encontradas.")
    else:
        for movimento in extrato:
            print(movimento[0])
        print(f'Saldo final: R$ {str(saldo).format(5.2)}')

while True:
    operacao=input('''
    Selecione a operação desejada:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
>>''')
    if operacao=='d':
        print('Informe o valor: ')
        depositar(float(input()))
    if operacao=='s':
        print('Informe o valor: ')
        sacar(float(input()))
    if operacao=='e':
        imprimeExtrato()
    if operacao=='q':
        break
    else:
        print('Escolha uma opção válida')
import uuid

class Reserva:
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Idade: {self.idade}"

def criarReserva():
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    id = uuid.uuid4()
    if idade >= 18:
        novaReserva = Reserva(id, nome, idade)
        reservas.append(novaReserva)
        print('Reserva criada.')
    else: print('A idade precisa ser igual maior que 18 anos, voltando...')

def listarReservas():
    if not reservas:
        print('Não há reservas.')
    for reserva in reservas:
        print (reserva)

def editarReserva():
    idEditar = input('Digite o ID da reserva que deseja alterar: ')
    for reserva in reservas:
        if str(reserva.id) == idEditar:
            while True:
                print('''    [1] Nome
    [2] Idade
    [3] Sair''')
                opcao = int(input('Escolha uma opção: '))
                match opcao:
                    case 1:
                        novoNome = str(input('Digite o novo nome: '))
                        reserva.nome = novoNome
                        print('Nome alterado.')
                    case 2:
                        novaIdade = int(input('Digite a nova idade: '))
                        if novaIdade >=18:
                            reserva.idade = novaIdade
                            print('Idade alterada.')
                        else: print('A nova idade deve ser maior ou igual a 18, voltando...')
                    case 3:
                        return
                    case _:
                        print('Opção inválida')
    else: print('Reserva não encontrada.')

def excluirReserva():
    idExcluir = input('Digite o ID da reserva que deseja excluir: ')
    for reserva in reservas:
        if str(reserva.id) == idExcluir:
            reservas.remove(reserva)
            print('Reserva removida.')
            return
    else: print('Reserva não encontrada.')
    

reservas = []

while True:
    print('''    [1] Criar uma nova reserva
    [2] Listar reservas
    [3] Editar reserva
    [4] Excluir reserva
    [5] Sair do programa''')
    
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1: 
            criarReserva()
        case 2: 
            listarReservas()
        case 3: 
            editarReserva()
        case 4: 
            excluirReserva()
        case 5: 
            print('Encerrando...')
            break
        case _:
            print('Opção inválida, voltando...')

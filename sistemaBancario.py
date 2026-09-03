import json 
menu = True

def mostrar_Menu_Principal():
    print("\n---Sistema Bancário---")
    print("1- Criar conta")
    print("2- Acessar conta")
    print("3- Esqueci minha senha")
    print("4- Sair")

def transferencia(usuarios,usuario_logado):
    usuario_destino = None
    print("\n-- Transferência bancária")

    transferir_user = str(input("Digite o login do usuário que voce deseja transferir: "))
    try:
        transferir_valor = float(
        input("Digite a quantidade que você deseja transferir: ")
    )
    except ValueError:
        print("Digite um valor numérico válido.")
        return
    if transferir_valor <= 0: 
        print("A quantia não pode ser negativa ")
        return 
    for usuario in usuarios:
        if transferir_user.upper() == usuario["nome"].upper():
            usuario_destino = usuario
            break
    if usuario_destino == usuario_logado: 
        print("Não é possível transferir para a sua própria conta")
        return 
    if usuario_destino is None: 
        print("Usuário de destino da transferência não foi encontrado")
        return
    if transferir_valor > usuario_logado["saldo"]:
        print("Seu saldo é insuficiente para essa transferência!")
        return
    if transferir_valor <= usuario_logado["saldo"]:
        usuario_logado["saldo"] = usuario_logado["saldo"] - transferir_valor
        usuario_destino["saldo"] = usuario_destino["saldo"] + transferir_valor
        extrato = f"Transferência de R${transferir_valor:.2f}"
        usuario_logado["extrato"].append(extrato)
        extrato = f"Recibo de R${transferir_valor:.2f} feito por {usuario_logado['nome']}"
        usuario_destino["extrato"].append(extrato)
        salvar_usuario(usuarios)
        print("Valor Transferido!")
        


def cadastrar():

    print("\n---Crie Sua conta!---")

    user = input("Escolha um nome de usuário: ").strip()
    cpf = input("Qual o seu CPF (apenas números): ").strip()

    # Validação de campos vazios
    if user == "":
        print("Erro: o nome de usuário não pode estar vazio!")
        return

    if cpf == "":
        print("Erro: o CPF não pode estar vazio!")
        return

    # Validação de CPF numérico
    if not cpf.isdigit():
        print("Erro: o CPF deve conter apenas números!")
        return

    # Validação de CPF duplicado e login duplicado
    for usuario in usuarios:

        if cpf == usuario["cpf"]:
            print("Erro: este CPF já está cadastrado!")
            return

        if user == usuario["nome"]:
            print("Erro: este nome de usuário já está em uso!")
            return

    senha = input("Escolha uma senha: ").strip()

    # Validação de senha vazia
    if senha == "":
        print("Erro: a senha não pode estar vazia!")
        return

    try:
        saldo = float(input("Saldo inicial da conta: "))

        if saldo < 0:
            print("Erro: o saldo inicial não pode ser negativo!")
            return

    except ValueError:
        print("Erro: digite um valor numérico válido para o saldo!")
        return

    new_usuario = {
        "nome": user,
        "cpf": cpf,
        "senha": senha,
        "saldo": saldo,
        "extrato": []
    }

    usuarios.append(new_usuario)
    salvar_usuario(usuarios)

    print("Conta criada com sucesso!")

def salvar_usuario(usuarios):
    with open ("dados.json", "w") as arquivo:
        json.dump(usuarios,arquivo)

def carregar_usuarios():
    with open ("dados.json", "r") as arquivo:
        usuarios = json.load(arquivo)
    return usuarios

def acessarConta():
    print("\n---Login---")
    login_usuario = input("Digite seu login: ")
    senha_usuario = input("Digite sua senha: ")
    for usuario in usuarios:
        if (
            login_usuario == usuario["nome"]
            and senha_usuario == usuario["senha"]
        ):

            print("Login realizado com sucesso!")
            return usuario
    print("Login inválido!")
    return None


def depositar(usuario):
    print("\n---Depósito---")
    deposito = float(input("Valor: "))
    usuario["saldo"] += deposito
    extrato = f"Depósito de R${deposito:.2f}"
    usuario["extrato"].append(extrato)
    salvar_usuario(usuarios)
    print("Valor depositado!")


def sacar(usuario):

    print("\n---Saque---")
    saque = float(input("Valor: "))
    if saque > usuario["saldo"]:
        print("Saldo insuficiente!")
    else:
        usuario["saldo"] -= saque
        extrato = f"Saque de R${saque:.2f}"
        usuario["extrato"].append(extrato)
        salvar_usuario(usuarios)
        print("Valor sacado!")


def mostrar_Extrato(usuario):

    print("\n---Extrato---")

    if len(usuario["extrato"]) == 0:
        print("Nenhuma movimentação encontrada.")

    else:
        for movimentacao in usuario["extrato"]:
            print(movimentacao)


def consultar_Saldo(usuario):
    print(f"\nSeu saldo é de R${usuario['saldo']:.2f}")


def resgatar_Senha():

    print("\n---Recuperação de Senha---")
    cpf = input("Digite seu CPF: ")
    login = input("Digite seu login: ")

    for usuario in usuarios:

        if cpf == usuario["cpf"] and login == usuario["nome"]:
            nova_senha = input("Digite sua nova senha: ")
            usuario["senha"] = nova_senha
            salvar_usuario(usuarios)
            print("Senha alterada com sucesso!")
            return
    print("CPF ou login inválidos!")

usuarios = carregar_usuarios()

while menu:

    mostrar_Menu_Principal()

    opcaoMenu = input("Escolha uma opção: ")

    if opcaoMenu == "1":
        cadastrar()

    elif opcaoMenu == "2":
        usuario_logado = acessarConta()

        if usuario_logado:

            acessar = True

            while acessar:

                print(f"\nBem vindo, {usuario_logado['nome']}")

                print("1- Depositar")
                print("2- Sacar")
                print("3- Ver extrato")
                print("4- Consultar saldo")
                print("5- Transferência")
                print("6- Sair")

                opcaoAcessar = input("Escolha uma opção: ")

                if opcaoAcessar == "1":
                    depositar(usuario_logado)

                elif opcaoAcessar == "2":
                    sacar(usuario_logado)

                elif opcaoAcessar == "3":
                    mostrar_Extrato(usuario_logado)

                elif opcaoAcessar == "4":
                    consultar_Saldo(usuario_logado)
                
                elif opcaoAcessar == "5":
                    transferencia(usuario_logado, usuarios)

                elif opcaoAcessar == "6":
                    print("Saindo da conta...")
                    acessar = False

                else:
                    print("Opção inválida!")

    elif opcaoMenu == "3":

        resgatar_Senha()

    elif opcaoMenu == "4":

        print("Programa encerrado!")
        menu = False

    else:

        print("Opção inválida!")
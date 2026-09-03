<<<<<<< HEAD
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
#-------------------------------------------------------------
menu = True
acessar = False
usuarios = []

while menu:
    print("---Sistema Bancário---")
    print("1- Criar conta")
    print("2- Acessar conta")
    print("3- Esqueci minha senha")
    print("4- Sair")
    opcaoMenu = str(input("Escolha uma opção: "))

    if opcaoMenu == "1":
            print("---Crie Sua conta!---")
            user = str(input("Escolha um nome de usuário:"))
            cpf = str(input("Qual o seu cpf (apenas números): "))
            senha = str(input("Escolha uma senha: "))
            saldo = float(input("Saldo inical do conta: "))
            new_usuario = {
                  "nome": user,
                  "cpf" : cpf,
                  "senha": senha,
                  "saldo": saldo,
                  "extrato": []
            }
            usuarios.append(new_usuario)
            print("Conta criada, parabéns!")

    elif opcaoMenu == "2": 
          
          #Verificar o login
          print("Qual seu login?")
          login_usuario = str(input("Digite o login aqui: "))
          print("Qual a sua senha")
          senha_usuario = str(input("Digite a senha aqui: "))
          for usuario in usuarios:
            if senha_usuario == usuario["senha"] and login_usuario == usuario["nome"]:

                menu = False
                acessar = True
                while acessar: 
                        print("Bem vindo a sua conta", usuario["nome"])
                        print("1- Depositar")
                        print("2- Sacar")
                        print("3- Ver estrato")
                        print("4- Consultar saldo")
                        print("5- sair")
                        opcaoAcessar = str(input("Escolha um opção: "))

                        if opcaoAcessar == "1": 
                            print("Digite o valor a ser depositado")
                            deposito = float(input("Valor: "))
                            usuario["saldo"] = deposito + usuario["saldo"]
                            extrato = f"Depósito de {deposito} reais"
                            usuario["extrato"].append(extrato)
                            print("Valor depositado!")
                            
                        
                        elif opcaoAcessar == "2": 
                            print("Quanto deseja sacar?")
                            saque = float(input("Valor: "))
                            if saque > usuario["saldo"]:
                                print("Seu saldo é insuficiente para esse valor")
                            else:
                                usuario["saldo"] = usuario["saldo"] - saque
                                extrato = f"Saque de {saque} reais"
                                usuario["extrato"].append(extrato)
                                print("Valor sacado!")
                            
                        
                        elif opcaoAcessar =="3": 
                            print(usuario["extrato"])
                        
                        elif opcaoAcessar == "4":
                            print(f"Seu saldo é de:", usuario["saldo"])
                        
                        elif opcaoAcessar == "5": 
                            print("Ok, saindo...")
                            acessar = False
                            menu = True
                            break
                        
                        else: 
                             print("Opção inválida, tente de novo por favor!")
            else: 
                 print("Login inválido, tente novamente por favor ")

    elif opcaoMenu == "3":
         resgatar_senha_CPF = str(input("Olá, para criar uma nova senha primeiro digite o seu cpf: "))
         resgatar_senha_Login = str(input("Agora digite o seu login: "))
         for usuario in usuarios:
            if resgatar_senha_CPF == usuario["cpf"] and resgatar_senha_Login == usuario["nome"]:
                nova_senha = str(input("Digite a sua nova senha aqui: "))
                usuario["senha"] = nova_senha
                print("senha altera com sucesso!")
            else: 
                 print("Login ou cpf inválidos, tente novamente po favor")


    elif opcaoMenu == "4": 
          print("Programa encerrado!")
          menu = False
          break
    else: 
         print("Opção inválida, tente de novo por favor!")


>>>>>>> 4ab4daaaad45c884e1e006d7dafc5091492692d8

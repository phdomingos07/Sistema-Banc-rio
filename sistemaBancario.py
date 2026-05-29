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



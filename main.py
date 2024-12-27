
v_nome = False


while v_nome is not True:
    
    try:
        nome = input("Digite seu nome: ")
        if nome.isspace():
            print("Seu nome está em branco")
        elif any(char.isdigit() for char in nome):
            print("Seu nome está com número")
        else:
            v_nome = True
            print(nome)
    except ValueError as e:
        print(e)
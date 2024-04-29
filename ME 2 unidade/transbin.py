while True:
    print("Tranformando um número inteiro em binário. ")
    sleep(1)
    numero = int(input("Insira um número inteiro: "))
    sleep(1)
    b = bin(n)
    if n == 0:
        print("Encerrado o programa")
        break
    print(f"O número {numero} convertido para binário equivale a {str(b)[2:]}")

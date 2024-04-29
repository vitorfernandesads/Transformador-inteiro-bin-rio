while True:
    print("Tranformando um número inteiro em binário. ")
    sleep(1)
    n = int(input("Insira um número inteiro: "))
    sleep(1)
    x = bin(n)
    if n == 0:
        print("Encerrado o programa!")
        break
    print(f"O número {n} convertido para binário equivale a {str(x)[2:]}")

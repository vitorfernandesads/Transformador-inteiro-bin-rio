from time import sleep
while True:
    print("Convertendo um número inteiro em binário.")
    sleep(1)
    numero = int(input("Insira um número inteiro: "))
    sleep(1)
    b = bin(n)
    if n == 0:
        print(" Fim do programa")
        break
    print(f"O número {numero} convertido para binário equivale à {str(b)[2:]}")

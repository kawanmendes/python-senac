def fibbonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b , a + b
        if a > n:
            break
    
numero = int(input("Digite um numero: "))
fibbonacci(numero)    
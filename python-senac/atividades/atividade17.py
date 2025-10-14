p1 = int(input("informe o primeiro numero"))
ul = float(input("informe o ultimo numero"))
ic = float(input("informe o incremento"))

if p1 <= ul:
    while p1 <= ul:
        print(p1)
        p1 = p1 + ic

else:
    while p1 >= ul:
        print(p1)
        p1 = p1 - ic
print("acabou!!!!")

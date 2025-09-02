c = "sim"
x= 1
while c == "sim":
  numero = int(input("informe o numero da tabada :"))

  for contador in range(1,11):
    numero * x
    print(numero * x)
    x += 1

  c = input("deseja continuar")
print("fim")
# Verificação de idade
nome = input("Digite seu nome aqui:")
nome_maiusculo = nome.upper()
idade = int(input("Digite sua idade aqui:"))

print(f"Seu nome é: {nome_maiusculo}, Sua idade é: {idade} anos")

if idade >= 18:
    print("Você é maior de idade!")
elif idade <= 10:
    print(f"Você tem: {idade}, portanto você é criança!")
else:
    print("Você é menor de idade!")
    


# Lista de Exercícios (10/10)

#1 - Crie uma função que calcule o fatorial de um número dado pelo usuário.
# def fatorial(n):
#     if n < 0:
#         return "Deu RUIM, n pode ser negativo"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         resultado = 1
#         for i in range(2, n + 1):
#             resultado *= i
#         return resultado
# num = int(input("Digite um número: "))
# print(f"O fatorial de {num} é {fatorial(num)}.")

#############################################################################################################################################
#2 - Desenvolva um programa que mostre a tabuada de um número informado pelo usuário.
# def tabuada (num):
#     for i in range (1,11):
#         result = num * i
#         print(f"{num} X {i} =",result)
#         i += 1
# num = int(input("Digite um número: "))
# tabuada(num)

#############################################################################################################################################
#3 - Escreva uma função que verifique se uma palavra ou frase é um palíndromo (pode ser lida da mesma maneira de trás para frente).
# def palindromo(frase):
#     return frase == frase[::-1]

# entrada = input("Digite a palavra: ")
# if palindromo(entrada):
#     print("É um palíndromo!")
# else:
#     print("Não é um palíndromo.")

#############################################################################################################################################
#4 - Faça um programa que verifique se um número fornecido é primo.
# def primo(entrada):
#     if entrada <= 1:
#         print(f"O número {entrada} não é primo!")
#         return
    
#     for i in range(2, int(entrada**0.5) + 1):
#         if entrada % i == 0:
#             print(f"O número {entrada} não é primo!")
#             return
    
#     print(f"O número {entrada} é primo!")

# entrada = int(input("Digite o número: "))
# primo(entrada)
#############################################################################################################################################
#5  - Desenvolva uma função que mostre os n primeiros termos da sequência de Fibonacci, onde n é informado pelo usuário.
# def fibonacci(n):
#     a, b = 0, 1
#     sequencia = []
#     for _ in range(n):
#         sequencia.append(a)
#         a, b = b, a + b  
#     return sequencia
# n = int(input("Digite o número da sequência de Fibonacci que vc quer ver: "))
# if n <= 0:
#     print("Por favor, digite um número positivo.")
# else:
#     termos = fibonacci(n)
#     print(f"Os primeiros {n} da sequência de Fibonacci são: {termos}")

#############################################################################################################################################
#6 - Escreva um algoritmo que receba uma lista de números e retorne a lista ordenada de forma crescente (Bubble sort).
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))
lista_ordenada = bubble_sort(numeros)
print("Lista ordenada:", lista_ordenada)

#############################################################################################################################################
#7 - Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa. O usuário deverá escolher a conversão desejada.

#8 - Crie um algoritmo que receba 5 números e exiba o maior e o menor número informados
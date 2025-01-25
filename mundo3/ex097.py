from os import system

def escreva(palavra):
    system('cls')
    a = int(len(palavra))
    print('~'*a)
    print(palavra)
    print('~'*a)
while True:
    escreva(input())

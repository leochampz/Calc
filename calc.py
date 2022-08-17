#By Champz!!!
#Feel free to improove.

def soma(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mult(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)
    

n1 = int(input('Qual o primeiro número: '))
n2 = int(input('informe o segundo número: '))
operador = input('Qual operação você deseja fazer: +,-,*,/ ?')

if operador == '+':
    soma(n1,n2)
if operador == '-':
    sub(n1,n2) 
if operador == '*':
    mult(n1,n2)
if operador == '/':
    div(n1,n2)

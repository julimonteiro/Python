'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))

cal = (n1 + n2) / 2

if cal < 5:
    print('Reprovado')
elif cal >= 5 and cal <= 6.9:
    print('Recuperação')
if cal >= 7:
    print('Aprovado') 
    
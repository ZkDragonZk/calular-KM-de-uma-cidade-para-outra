import time
import os

print('====== PAINEL DE KM ======')

print('')
# SUA ESCOLHA DE CIDADE
cidadeatual = (input('Digite Sua Cidade: '))
cidadequevai = (input('Digite A Outra Cidade: '))
print('')
os.system('cls')
# SEGUNDA PARTE DE CALCULO
kminicial = int(input('Digite a KM Inicial: '))
kmfinal = int(input('Digite a KM final: '))
resultado1 = kminicial - kmfinal
print('KM Rodados foi de {}'.format(resultado1))
time.sleep(4)
os.system('cls')
# TANQUE
litros = int(input('Digite Quantos Usou Para Encher o Tanque exemplo 29 LT:  '))
resultado2 = resultado1 / litros
print('Média KM/L foi de {}'.format(resultado2))
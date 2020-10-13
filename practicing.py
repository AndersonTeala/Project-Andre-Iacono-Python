# -*- coding: utf-8 -*-
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
esporte = input('Digite seu esporte favorito: ')
fome = input('Digite sua comida preferida: ')

print('\nFicha Tecnica do Cliente\n')
print(nome)
print(idade)
print(esporte)
print(fome)

print('\nInformacoes\n')
print('Cliente ' + nome + ',' 'tem a idade de ' + idade + ' anos,' ' e gosta de ' + esporte + ' nas suas horas vagas.' ' E adora comer ' + fome + ' quando esta com fome.\n')

if (int(idade) > 20):
    print('Voce ' + nome + ' esta chegando na idade')
else:
    print('Parabens ' + nome + ' Você é jovem ainda, jovem ainda, jovem ainda Amanhã velho será, velho será, velho será! A menos que o coração, que o coração sustente A juventude que nunca morrerá!')
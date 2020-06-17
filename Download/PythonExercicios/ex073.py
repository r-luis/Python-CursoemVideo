'''Desafio 73 Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Brasileirão, na ordem de colocação. Depois mostre:

Apenas os 5 primeiros colocados.
Os últimos 4 colocados da tabela.
Uma lista com os times em ordem alfabética.
Em que posição na tabela está o time da Chapecoense.'''
div = ('-'*50)
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico', 'São Paulo', 'Intenacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(div)
print('Campeonato Brasileiro')
print(div)
print(f'5 primeiros colocados: {times[0:5]}')
print(div)
print(f'4 últimos colocados: {times[16:20]}')
print(div)
print(sorted(times))
print(div)
print(f'Posição da Chapecoense: {times.index("Chapecoense")}º Lugar')
print(div)

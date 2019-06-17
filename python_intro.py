
if 5 > 2: 
	print('5 é maior que 2')
else:
	print('5 não e maior que 2')


name = ''
if (name == 'Ola'):
	print('Olá, Ola!')
elif (name == 'Lucas'):
	print('Olá, Lucas!')
else:
	print('Olá Estranho')


volume = 57
if volume < 20:
	print('Está um pouco baixo')
elif 20 <= volume < 40:
	print('Está bom para música ambiente')
elif 40 <= volume < 60:
	print('Perfeito, posso ouvir todos os detalhes')
elif 60 <= volume < 80:
	print('Ótimo para festas!')
elif 80 <= volume < 100:
	print('Está muito alto!')
else:
	print('Meus ouvidos doem! :(')


#Mudar o volume se estiver muito alto e muito baixo
volume = 100
if volume < 20 or volume > 80:
   print('Bem melhor!')

girls = ['Rachel, Monica, Thayane, Nay, Ola']
print(girls)


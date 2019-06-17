#Função sem parâmetro

def oi():
	print('Olá mundo!')
	print('Tudo bem ?')

oi()


#Função com parâmetro

def oi(nome):
	if nome == "ola":
		print('Olá, Ola')
	elif nome == "Lucas":
		print('Olá, Lucas')
	else:
		print('Olá Estranho')
oi('Sonja')

#

def oi(name):
	print('Olá , ' + name + '!')
oi('Rachel')


def oi(nome):
	print('Oi ' + nome + '!')
	
girls = ['Rachel, Monica, Thayane, Nay, Ola']
for name in girls:
	oi(name)
	print('Proxima')
oi('Floretina, Julya, Alice e Flora ')

#Usando for para números usando a funcão Range
for i in range(1, 6):
	print(i)
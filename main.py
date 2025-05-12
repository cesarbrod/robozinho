# Um robozinho para responder tuas perguntas

# Precisamos de aleatoriedade

import random

# Armazenando variáveis

olas = ['Olá ', 'Oi ', 'Salve ', 'E aí ', 'Opa ', 'Aê ']
tchaus = ['Tchau!', 'Até logo!', 'Até mais!', 'Até breve!', 'Bora!', 'Adeus!']
chaves = ['música', 'rock', 'mãe', 'programação']
respostas = ['Adoro música!', 'Rock não é coisa do diabo?', 'Senti uma vive meio edipiana na nossa conversa...', 'Ei!!! Eu sou um programa! :-)']
             
# Boas vindas ao usuário
print("Oi! Eu sou o robozinho!")

# Com quem estou falando?
nome = input("Com quem estou falando? ")

# Robozinho saúda a pessoa
print(random.choice(olas) + nome +"!")

# Verificando se é a Maria
if nome == "Maria":
  print("Esse também é o nome da minha melhor amiga!")
else:
  print("Espero que o mundo esteja te tratando bem!")

r_usuario = input("Sobre o que vovê quer conversar agora? ")
r_usuario = r_usuario.lower()

while (r_usuario != "tchau"):
  chave_encontrada = False
  
  for indice in range(len(chaves)):
    if (chaves[indice] in r_usuario):
      print("Robozinho: " + respostas[indice])
      chave_encontrada = True

  if (chave_encontrada == False):
    nova_chave = input("Robozinho: Desculpe, ainda não sei falar sobre esse assunto. Qual é a palavra-chave principal da sua pergunta (apenas uma)? ")
    chaves.append(nova_chave)
    nova_resposta = input("Robozinho: E qual resposta você recomenda para essa palavra-chave? ")
    respostas.append(nova_resposta)
    print("Robozinho: Obrigado por me ajudar a conversar melhor! ")

  r_usuario = input("Sobre o que você quer conversar agora? - digite tchau para terminar: ")
  r_usuario = r_usuario.lower()

print(random.choice(tchaus))

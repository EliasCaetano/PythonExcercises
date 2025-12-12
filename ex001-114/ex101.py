from datetime import datetime

def voto(ano):
      nasc = datetime.now().year - ano
      if nasc < 16:
          return f'Com {nasc} anos, o voto é NEGADO'
      elif nasc > 16 and nasc < 18:
          return f'Com {nasc} anos, o voto é OPCIONAL'
      elif nasc >= 18 and nasc < 65:
          return f'Com {nasc} anos, o voto é OBRIGATÓRIO'
      elif nasc >= 65:
          return f'Com {nasc} anos, o voto é OPCIONAL'


#MAIN PROGRAM
ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))


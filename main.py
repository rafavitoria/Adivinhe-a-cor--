import random
while(True):
   pontos_seus = 0
   pontos_dele = 0
   cor_secreta = random.choice(['R', 'G', 'B'])
   palpite = input("Adivinhe a cor ('R', 'G', e 'B'): ").upper()
   if palpite not in ['R', 'G', 'B']:
      print("Entrada invalida. Escolha R, G ou B.")
   elif palpite == cor_secreta:
     print("parabens! Voce acertou!")
     pontos_seus = pontos_seus + 1
   else:
     print('ERROU!!!!!!!!!')
     pontos_deles = pontos_dele + 1
     print('A cor era ', cor_secreta)
     print(f'VOCE {pontos_seus} x PC {pontos_deles}')
from pygame import mixer, event
from datetime import time
mixer.init()
print('\033[1;34mTocando...')
time(1)
mixer.music.load('10_Eu_Jamais_Serei_o_Mesmo_Onde_Quer_Que_For_Irei_Acústico.mp3')
mixer.music.play(0)
input()
event.wait()